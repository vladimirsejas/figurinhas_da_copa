"""
Sistema de Album de Figurinhas - Copa 2026
Disciplina: Estrutura de Dados | FATEC Rio Claro
"""

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich import box

from src.figurinha import Figurinha
from src.album import Album
from src.fila import Fila
from src.historico import Historico
from src import persistencia

console = Console()

BANDEIRA = (
    "[green]████████████████████████████[/]\n"
    "[green]██████[/][yellow]████████████[/][green]██████[/]\n"
    "[green]████[/][yellow]██████████████████[/][green]████[/]\n"
    "[green]██████[/][yellow]████[/][blue] ████ [/][yellow]████[/][green]██████[/]\n"
    "[green]████[/][yellow]██████████████████[/][green]████[/]\n"
    "[green]██████[/][yellow]████████████[/][green]██████[/]\n"
    "[green]████████████████████████████[/]"
)


def exibir_banner():
    console.print(Panel(Align.center(BANDEIRA), border_style="green"))
    console.print(Panel(
        Align.center(
            "[bold yellow]SISTEMA DE ALBUM DE FIGURINHAS[/]\n"
            "[bold green]COPA DO MUNDO 2026[/]\n"
            "[dim]Estrutura de Dados - FATEC Rio Claro[/]"
        ),
        border_style="yellow",
        box=box.DOUBLE
    ))


def exibir_menu_principal():
    console.print(Panel(
        "[bold yellow]1.[/] Album\n"
        "[bold yellow]2.[/] Figurinhas repetidas\n"
        "[bold yellow]3.[/] Trocas\n"
        "[bold yellow]4.[/] Salvar dados\n"
        "[bold red]0.[/] Sair",
        title="[bold green]MENU PRINCIPAL[/]",
        border_style="green",
        box=box.ROUNDED
    ))


def exibir_menu(titulo, opcoes):
    texto = "\n".join(
        f"[bold yellow]{k}.[/] {v}" for k, v in opcoes.items()
    )
    console.print(Panel(texto, title=f"[bold green]{titulo}[/]",
                        border_style="yellow", box=box.ROUNDED))


def criar_figurinha_manual():
    console.print(Panel("[bold]Nova Figurinha[/]", border_style="blue", box=box.SIMPLE))
    try:
        id_fig = int(console.input("[cyan]ID da figurinha:[/] "))
        if id_fig <= 0:
            console.print("[red]ID deve ser positivo.[/]")
            return None
    except ValueError:
        console.print("[red]ID invalido.[/]")
        return None

    nome     = console.input("[cyan]Nome do jogador:[/] ").strip()
    pais     = console.input("[cyan]Pais/Selecao:[/] ").strip()
    posicao  = console.input("[cyan]Posicao (goleiro/defensor/meio/atacante):[/] ").strip().lower()
    raridade = console.input("[cyan]Raridade (comum/rara/lendaria):[/] ").strip().lower()

    if posicao not in {"goleiro", "defensor", "meio", "atacante"}:
        console.print("[red]Posicao invalida.[/]")
        return None
    if raridade not in {"comum", "rara", "lendaria"}:
        console.print("[red]Raridade invalida.[/]")
        return None

    return Figurinha(id_fig, nome, pais, posicao, raridade)


def exibir_album_tabela(album):
    tabela = Table(title="Album da Copa 2026", box=box.ROUNDED,
                   border_style="green", show_lines=True)
    tabela.add_column("ID",       style="bold cyan",   justify="center")
    tabela.add_column("Jogador",  style="bold white")
    tabela.add_column("Pais",     style="yellow")
    tabela.add_column("Posicao",  style="blue")
    tabela.add_column("Raridade", style="magenta")

    cores = {"lendaria": "gold1", "rara": "cyan1", "comum": "white"}

    atual = album._cabeca
    while atual is not None:
        f = atual.figurinha
        cor = cores.get(f.raridade, "white")
        tabela.add_row(
            str(f.id),
            f"[{cor}]{f.nome}[/]",
            f.pais,
            f.posicao,
            f"[{cor}]{f.raridade}[/]"
        )
        atual = atual.proximo

    if album.tamanho() == 0:
        console.print(Panel("[yellow]O album esta vazio.[/]", border_style="yellow"))
    else:
        console.print(tabela)


def exibir_progresso(album):
    pct = (album.tamanho() / 640) * 100
    with Progress(
        TextColumn("[bold green]Progresso do album"),
        BarColumn(bar_width=40, style="yellow", complete_style="green"),
        TextColumn(f"[bold]{album.tamanho()}/640 ({pct:.1f}%)[/]"),
    ) as progress:
        task = progress.add_task("", total=640)
        progress.update(task, completed=album.tamanho())
    console.print()


def menu_album(album, repetidas):
    while True:
        console.print()
        exibir_menu("ALBUM", {
            "1": "Colar figurinha",
            "2": "Remover figurinha",
            "3": "Consultar por ID",
            "4": "Ver album completo",
            "5": "Ver progresso",
            "6": "Buscar por jogador",
            "7": "Buscar por selecao",
            "0": "Voltar"
        })
        opcao = console.input("[bold green]Opcao:[/] ").strip()

        if opcao == "1":
            fig = criar_figurinha_manual()
            if fig:
                album.adicionar(fig)

        elif opcao == "2":
            try:
                id_fig = int(console.input("[cyan]ID para remover:[/] "))
                album.remover(id_fig)
            except ValueError:
                console.print("[red]ID invalido.[/]")

        elif opcao == "3":
            try:
                id_fig = int(console.input("[cyan]ID a consultar:[/] "))
                fig = album.buscar(id_fig)
                if fig:
                    console.print(Panel(str(fig), border_style="cyan"))
                else:
                    console.print("[red]Figurinha nao encontrada.[/]")
            except ValueError:
                console.print("[red]ID invalido.[/]")

        elif opcao == "4":
            exibir_album_tabela(album)

        elif opcao == "5":
            exibir_progresso(album)

        elif opcao == "6":
            nome = console.input("[cyan]Nome do jogador:[/] ").strip()
            resultado = album.buscar_por_jogador(nome)
            if resultado:
                no = resultado
                while no is not None:
                    console.print(Panel(str(no.figurinha), border_style="cyan"))
                    no = no.proximo
            else:
                console.print("[red]Nenhuma figurinha encontrada.[/]")

        elif opcao == "7":
            pais = console.input("[cyan]Pais/Selecao:[/] ").strip()
            resultado = album.buscar_por_selecao(pais)
            if resultado:
                no = resultado
                while no is not None:
                    console.print(Panel(str(no.figurinha), border_style="cyan"))
                    no = no.proximo
            else:
                console.print("[red]Nenhuma figurinha encontrada.[/]")

        elif opcao == "0":
            break
        else:
            console.print("[red]Opcao invalida.[/]")


def menu_repetidas(repetidas):
    while True:
        console.print()
        exibir_menu("REPETIDAS", {
            "1": "Adicionar repetida",
            "2": "Ver todas as repetidas",
            "3": "Contar repetidas",
            "0": "Voltar"
        })
        opcao = console.input("[bold green]Opcao:[/] ").strip()

        if opcao == "1":
            fig = criar_figurinha_manual()
            if fig:
                if fig.id not in repetidas:
                    repetidas[fig.id] = Fila()
                repetidas[fig.id].enqueue(fig)
                console.print(f"[green]Figurinha #{fig.id} adicionada as repetidas.[/]")

        elif opcao == "2":
            if not repetidas:
                console.print("[yellow]Nenhuma figurinha repetida.[/]")
            else:
                for id_fig, fila in repetidas.items():
                    tabela = Table(
                        title=f"Figurinha #{id_fig} - {fila.tamanho()} repetida(s)",
                        box=box.SIMPLE, border_style="yellow"
                    )
                    tabela.add_column("ID",       style="cyan",    justify="center")
                    tabela.add_column("Jogador",  style="white")
                    tabela.add_column("Pais",     style="yellow")
                    tabela.add_column("Posicao",  style="blue")
                    tabela.add_column("Raridade", style="magenta")
                    no = fila._inicio
                    while no is not None:
                        f = no.figurinha
                        tabela.add_row(str(f.id), f.nome, f.pais, f.posicao, f.raridade)
                        no = no.proximo
                    console.print(tabela)

        elif opcao == "3":
            total = sum(f.tamanho() for f in repetidas.values())
            console.print(Panel(
                f"[bold yellow]Total de figurinhas repetidas: {total}[/]",
                border_style="yellow"
            ))

        elif opcao == "0":
            break
        else:
            console.print("[red]Opcao invalida.[/]")


def menu_trocas(repetidas, historico):
    while True:
        console.print()
        exibir_menu("TROCAS", {
            "1": "Propor/efetuar troca",
            "2": "Ver historico de trocas",
            "0": "Voltar"
        })
        opcao = console.input("[bold green]Opcao:[/] ").strip()

        if opcao == "1":
            try:
                id_voce  = int(console.input("[cyan]ID da sua repetida:[/] "))
                id_outro = int(console.input("[cyan]ID da repetida do outro:[/] "))
            except ValueError:
                console.print("[red]ID invalido.[/]")
                continue

            tem_voce  = id_voce  in repetidas and not repetidas[id_voce].esta_vazia()
            tem_outro = id_outro in repetidas and not repetidas[id_outro].esta_vazia()

            if not tem_voce:
                console.print(f"[red]Voce nao tem a figurinha #{id_voce} como repetida.[/]")
            elif not tem_outro:
                console.print(f"[red]O outro nao tem a figurinha #{id_outro} como repetida.[/]")
            else:
                fig_voce  = repetidas[id_voce].dequeue()
                fig_outro = repetidas[id_outro].dequeue()
                repetidas.setdefault(fig_outro.id, Fila()).enqueue(fig_outro)
                repetidas.setdefault(fig_voce.id,  Fila()).enqueue(fig_voce)
                desc = (f"Troca: figurinha #{fig_voce.id} ({fig_voce.nome}) "
                        f"por #{fig_outro.id} ({fig_outro.nome})")
                historico.registrar(desc)
                console.print("[green]Troca efetuada com sucesso![/]")

        elif opcao == "2":
            historico.exibir()

        elif opcao == "0":
            break
        else:
            console.print("[red]Opcao invalida.[/]")


def main():
    album     = Album()
    repetidas = {}
    historico = Historico()

    dados_album, dados_repetidas = persistencia.carregar()
    for d in dados_album:
        fig = Figurinha(d["id"], d["nome"], d["pais"], d["posicao"], d["raridade"])
        album.adicionar(fig)
    for d in dados_repetidas:
        fig = Figurinha(d["id"], d["nome"], d["pais"], d["posicao"], d["raridade"])
        if fig.id not in repetidas:
            repetidas[fig.id] = Fila()
        repetidas[fig.id].enqueue(fig)

    while True:
        console.clear()
        exibir_banner()
        exibir_menu_principal()
        opcao = console.input("[bold green]Opcao:[/] ").strip()

        if opcao == "1":
            menu_album(album, repetidas)
        elif opcao == "2":
            menu_repetidas(repetidas)
        elif opcao == "3":
            menu_trocas(repetidas, historico)
        elif opcao == "4":
            persistencia.salvar(album, repetidas)
            console.print("[green]Dados salvos![/]")
        elif opcao == "0":
            persistencia.salvar(album, repetidas)
            console.print(Panel("[bold green]Ate logo![/]", border_style="green"))
            break
        else:
            console.print("[red]Opcao invalida.[/]")


if __name__ == "__main__":
    main()