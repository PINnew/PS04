import wikipediaapi

# Указываем язык и user_agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='ru',
    user_agent='My Wikipedia Bot/1.0 (https://mywebsite.com; contact@myemail.com)'
)


def search_article(article_name):
    """Функция поиска статьи на Википедии."""
    page = wiki_wiki.page(article_name)

    if not page.exists():
        print("Статья не найдена.")
        return None

    print(f"\nЗаголовок статьи: {page.title}\n")
    return page


def display_paragraphs(page):
    """Функция для вывода параграфов статьи."""
    sections = page.sections
    if not sections:
        print("У статьи нет параграфов.")
        return

    for section in sections:
        print(f"\nПараграф: {section.title}\n")
        print(section.text[:1000])  # Ограничим вывод текста до 1000 символов
        print("\n" + "-" * 80 + "\n")

        # Вопрос пользователю
        action = input("Продолжить чтение этой статьи (y/n)? ").lower()
        if action == 'n':
            break


def choose_linked_page(page):
    """Функция для перехода на одну из связанных страниц."""
    links = page.links
    linked_pages = list(links.keys())

    if not linked_pages:
        print("Связанных страниц нет.")
        return None

    print("\nСвязанные страницы:")
    for i, link in enumerate(linked_pages):
        print(f"{i + 1}. {link}")

    while True:
        try:
            choice = int(input("\nВведите номер страницы для перехода или 0 для выхода: ")) - 1
            if choice == -1:
                return None
            if 0 <= choice < len(linked_pages):
                selected_page = linked_pages[choice]
                return search_article(selected_page)
        except (ValueError, IndexError):
            print("Неверный ввод, попробуйте снова.")


def main():
    print("Добро пожаловать в Википедия поиск через консоль!")

    while True:
        initial_query = input("\nВведите запрос для поиска на Википедии: ")
        page = search_article(initial_query)

        if page is None:
            continue

        while True:
            print("\nЧто вы хотите сделать?")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")
            choice = input("Введите номер действия: ").strip()

            if choice == '1':
                display_paragraphs(page)
            elif choice == '2':
                linked_page = choose_linked_page(page)
                if linked_page:
                    page = linked_page
                else:
                    print("Возвращаемся в текущую статью...")
            elif choice == '3':
                print("Выход из программы. До свидания!")
                return
            else:
                print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
