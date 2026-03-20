from validate import TaskValidate
from sources import FileSource, GeneratorSource, APISource, IncorrectSource
from protocol import TaskSource


def main():
    validator = TaskValidate()

    file_source = FileSource("file.txt")
    gen_source = GeneratorSource(3)
    api_source = APISource("https://google.com")
    incor_source = IncorrectSource("sample")

    print("Проверка соответствия контракту:")
    for source in [file_source, gen_source, api_source, incor_source]:
        print(f"Подходит ли {source.__class__.__name__}:\n {isinstance(source, TaskSource)}")

    validator.add_source(file_source)
    validator.add_source(gen_source)
    validator.add_source(api_source)

    try:
        validator.add_source(incor_source)
    except TypeError as e:
        print(f"  Ошибка при добавлении IncorrectSource: {e}")

    tasks = validator.load_all_tasks()

    print("Список задач:")
    for task in tasks:
        print(f"{task.payload}")


if __name__ == "__main__":
    main()
