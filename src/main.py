import random
from src.validate import TaskValidate
from src.sources import FileSource, GeneratorSource, APISource, IncorrectSource
from src.protocol import TaskSource
from src.api_client import APIClient


def main():
    print("API Клиент:")
    client = APIClient()
    user = client.create_user()

    validator = TaskValidate()

    file_source = FileSource("file.txt")
    gen_source = GeneratorSource(3)
    api_source = APISource(limit=client.task_limit)
    incor_source = IncorrectSource("sample")

    for source in [file_source, gen_source, api_source, incor_source]:
        print(f"Подходит ли {source.__class__.__name__}: {isinstance(source, TaskSource)}")

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
        print(f"  [{task.id}] {task.payload}")


if __name__ == "__main__":
    main()