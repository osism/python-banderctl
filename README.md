# banderctl

`banderctl` is a tool used to manage [bandersnatch](https://github.com/pypa/bandersnatch) in a way, to use it as a offline mirror for pypi. bandersnatch itself is just a client, but it's container supports a periodic execution. What was missing, is an API that allows on-the-fly modification of the _bandersnatch.conf_ file to add or remove packages to be mirrored.

banderctl fills this gap by using [fastapi](https://github.com/tiangolo/fastapi). Currently there is only one endpoint:

## Usage

Use the client provided in this reposirtory underneath the folder `client`. Run it by using `python3 main.py --help`.

Example:

```shell
python3 main.py --endpoint http://example.com add -p osism
```

Of course you might also use the `http://example.com/docs` endpoint to perform API operations.

or you use `curl`:

```shell
#!/bin/bash
curl -X 'POST' \
  'https://example.com/allowlist/packages' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "mode": "add", "packages": ["osism"] }'
```

## Example deployment

Have a look inside the _example_ folder in this repository. There you'll find a docker-compose, but behind an nginx ingress. Therefore the paths change a bit.
The packages itself are hosted underneath `http://example.com/pip` while the API is reachable via `http://example.com/banderctl`

If you are looking for a helm chart, head over to our [helm-charts](https://github.com/osism/helm-charts).

## Settings

Have a look at the _settings.py_ to see the environment variables you can set.
