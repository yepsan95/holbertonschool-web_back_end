export default function handleResponseFromAPI(promise) {
  successObject = {
    status: 200,
    body: 'success',
  };
  return promise
    .then(() => successObject)
	.catch(() => new Error())
	.finally(() => console.log('Got a response from the API'));
}
