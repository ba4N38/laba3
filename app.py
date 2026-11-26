"""Веб-интерфейс калькулятора ипотеки для продуктового контура."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from calculator import calculate_monthly_payment

PAGE = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>Калькулятор ипотеки</title>
<style>
  body {{ font-family: Arial, sans-serif; max-width: 560px; margin: 40px auto; }}
  input {{ width: 100%; padding: 6px; margin: 4px 0 12px; }}
  button {{ padding: 8px 20px; }}
  .result {{ margin-top: 20px; font-size: 20px; color: #1a5d1a; }}
</style>
</head>
<body>
<h1>Калькулятор ипотеки</h1>
<form method="get">
  <label>Сумма кредита</label>
  <input name="principal" value="{principal}">
  <label>Годовая ставка, %</label>
  <input name="rate" value="{rate}">
  <label>Срок, лет</label>
  <input name="years" value="{years}">
  <button type="submit">Рассчитать</button>
</form>
<div class="result">{result}</div>
</body>
</html>"""


def render(principal="1000000", rate="10", years="10"):
    result = ""
    try:
        payment = calculate_monthly_payment(
            float(principal), float(rate), float(years)
        )
        result = f"Ежемесячный платёж: {payment:.2f} руб."
    except (ValueError, ZeroDivisionError):
        result = "Ошибка: проверьте введённые значения"
    return PAGE.format(
        principal=principal, rate=rate, years=years, result=result
    )


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        html = render(
            query.get("principal", ["1000000"])[0],
            query.get("rate", ["10"])[0],
            query.get("years", ["10"])[0],
        ).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(html)))
        self.end_headers()
        self.wfile.write(html)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
