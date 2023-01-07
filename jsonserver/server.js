const jsonServer = require("json-server");
const server = jsonServer.create();
const router = jsonServer.router("db.json");
const middlewares = jsonServer.defaults();

function sleep(ms) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

function getRandomResponse() {
	const random = Math.floor(Math.random() * 5);
	if (random < 3) {
		console.log("Отдаём ошибку");
		return true;
	}
	return false;
}

// Set default middlewares (logger, static, cors and no-cache)
server.use(middlewares);

// To handle POST, PUT and PATCH you need to use a body-parser
// You can use the one used by JSON Server
server.use(jsonServer.bodyParser);
server.use(async (req, res, next) => {
	switch (req.url) {
		case "/posts":
			{
				await sleep(1 * 1000);
			}
			break;
		case "/profile":
			{
				await sleep(2 * 1000);
			}
			break;
		case "/comments":
			{
				await sleep(3 * 1000);
			}
			break;
		case "/public_data":
			{
				await sleep(4 * 1000);
			}
			break;
		case "/danger_data":
			{
				await sleep(1 * 1000);
				if (getRandomResponse())
					res.status(500).send("Ошибка на стороне сервера 5хх");
			}
			break;
		default:
	}
	next();
});

// Use default router
server.use(router);
server.listen(3000, (err) => {
	if (err) console.log(err);
	console.log("JSON Server is running");
});
