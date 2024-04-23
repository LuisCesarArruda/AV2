generate_inner_join = lambda: """
SELECT *
FROM GAMES
INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company
"""

generate_select = lambda attributes: f"""
SELECT {', '.join(attributes)}
FROM GAMES
INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company
"""

if __name__ == "__main__":
    select_query = generate_select(["GAMES.title", "COMPANY.name"])
    print("Consulta SQL gerada:")
    print(select_query)
