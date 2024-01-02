import requests


def send_get_request(url):
    try:
        # Отправляем GET-запрос к указанному URL
        response = requests.get(url)

        # Проверяем успешность запроса (статус код 200)
        if response.status_code == 200:
            # Выводим содержимое ответа в консоль
            print("Ответ от сервера:")
            print(response.text)
        else:
            # Выводим сообщение об ошибке
            print(f"Ошибка при выполнении запроса. Статус код: {response.status_code}")

    except requests.RequestException as e:
        # Выводим сообщение об ошибке сети или других проблемах
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    # Введите URL сервера, к которому будет направлен запрос
    server_url = input("Введите URL сервера: ")

    # Вызываем функцию для отправки GET-запроса
    send_get_request(server_url)