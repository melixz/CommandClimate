# Получение погоды из терминала

Данный скрипт позволяет получить текущий прогноз погоды для выбранного города из терминала. Для этого используется библиотека requests и сервис [wttr.in](https://wttr.in/).

## Инструкции по использованию

1. Убедитесь, что у вас установлен Python и библиотека `requests`.

2. Сохраните скрипт `main.py` в удобном для вас месте.

3. Запустите скрипт из терминала:

   ```
   python main.py run
   ```

4. Когда вас попросят ввести название города, введите желаемый город (например, "Москва", "Лондон", "Шереметьево" или "Череповец").

5. Вы увидите текущий прогноз погоды для выбранного города прямо в терминале.

## Особенности

- Скрипт использует сервис [wttr.in](https://wttr.in/) для получения информации о погоде. Этот сервис предоставляет данные в удобном для чтения формате.
- Вы можете указывать любой город, для которого доступна информация на wttr.in.
- Обратите внимание, что сервис wttr.in может быть временно недоступен или предоставлять неполные данные. В этом случае скрипт выведет соответствующее сообщение.