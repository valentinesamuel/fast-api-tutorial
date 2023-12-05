# fast-api-tutorial

- Create a virtual env

```
python3 -m venv <PROJECT-NAME>
```

- Activate the virtual env

```
source <PROJECT-NAME>/bin/activate
```

- Install fastapi and all the deps

```
pip3 install fastapi[all]
```

- Show all install deps

```
pip3 freeze
```

- Start the web server

```
uvicorn main:app --reload
```

> "main" refers to the file main.py.

> "app" is the entry.

> "--reload" is a flag to reload the server when the code changes.
