export default function handleResponseFromAPI(promise) {
  const resolveObject = {
    status: 200,
    body: 'success',
  };
  return promise
    .then(() => resolveObject)
	.catch(() => new Error())
	.finally(() => console.log('Got a response from the API'));
}
