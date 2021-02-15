# obtencion, mantencion, ideas, etc. con informacion de digimon

## History

Me encanda Digimon, y ya existen muchos pokedeck's, pero pocos digideck's.

Este proyecto es un inicio de lo que podria ser un Digideck. el cual lo construi bajo el siguiente FramWork:

- cement

## Requeriments

- python 3.7
- pipenv

## Instalacion

```
$ pipenv install

$ pipenv run install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ pipenv install

$ pipenv shell


### run digimondata cli application

$ digimondata --help


### run pytest / coverage

$ make test
```


### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```
$ make dist

$ make dist-upload
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `digimon-data`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it digimondata --help
```
