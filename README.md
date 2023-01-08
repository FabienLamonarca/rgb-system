# rgb-system

## How to build application 🛠️

The only thing you will need should be **Docker** 🐋

```bash
# To build only kafka:
docker-compose --profile=kafka up -d --build

# To build all the app:
docker-compose --profile=full up -d --build


docker-compose up -d --build
```

## Time to clean up ? 🧽

```bash
docker-compose down -v --rmi all
```
