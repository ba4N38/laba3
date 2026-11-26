# Калькулятор ипотеки — CI/CD (ПР №3)

Учебный проект по практической работе «Настройка CI/CD».

## Состав

- `calculator.py` — расчёт ежемесячного аннуитетного платежа.
- `calculator_gui.py` — десктопный интерфейс на tkinter.
- `app.py` — веб-интерфейс для продуктового контура (порт 8000).
- `test_calculator.py`, `test_app.py` — тесты pytest.
- `.github/workflows/ci.yml` — пайплайн GitHub Actions.

## Пайплайн

`push` в `main` запускает:

1. **Lint & tests** — flake8 и 7 тестов pytest (расчёты и веб-интерфейс).
2. **Deploy** — публикация кода в `/opt/mortgage-calculator` на продуктовом
   контуре, перезапуск systemd-сервиса и smoke-тест на порту 8000.

Все job'ы выполняются на self-hosted runner'е, установленном на продуктовой
виртуальной машине (Ubuntu, Docker).

## Локальный запуск

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest -v
.venv/bin/python app.py      # http://localhost:8000
```
