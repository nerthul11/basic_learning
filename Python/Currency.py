import requests

def main():
    var = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR")
    print(var.status_code)
    if var.status_code != 200:
        raise Exception("Unsuccesful request. Try again.")
    data = var.json()

    print(data)

if __name__ == "__main__":
    main()