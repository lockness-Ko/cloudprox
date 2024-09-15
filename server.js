export default {
  async fetch(request, env, ctx) {
    const upgradeHeader = request.headers.get('Upgrade');
    if (!upgradeHeader || upgradeHeader !== 'websocket') {
      return new Response('Expected Upgrade: websocket', { status: 426 }); 
    }

    const webSocketPair = new WebSocketPair();
    const [client, server] = Object.values(webSocketPair);

    server.accept();
    server.addEventListener('message', async (event) => {
      let data = JSON.parse(event.data.toString());

      let res = await fetch(data.url, {headers: data.headers, body: data.body, method: data.method});
      let content = await res.text();
      server.send(content);
    }, false);

    return new Response(null, {
      status: 101,
      webSocket: client,
    });
  },
};
