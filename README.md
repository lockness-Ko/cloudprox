# cloudprox
Use cloudflare workers for a forever IP rotating proxy.

# Usage

Designed to be pretty much a copy of the 'curl' utility.

e.g.
```bash
./cloudprox.py -X POST -H "Cool: totally" -A "SecretAgent12" https://my.cool.url/?a=1
```

1. Create a cloudflare worker.

2. Upload the contents of server.js to your cloudflare worker :)

3. Profit! Set the proxy either with the CLOUDPROX_URL environment variable or by passing it as an argument with `-p` or `--proxy`:

```bash
export CLOUDPROX_URL=wss://my-cloudprox-endpoint
# some time later....
./cloudprox.py https://cool.com

# OR

./cloudprox.py --proxy 'wss://my-cloudprox-endpoint' https://cool.com
```
