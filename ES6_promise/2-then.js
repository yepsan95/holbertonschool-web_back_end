export default function handleResponseFromAPI(promise) {
  const successObject = {
    status: 200,
    body: 'success',
  };
  return promise
    .then(() => {
      return successObject;
    }
	.catch(() => new Error())
	.finally(() => console.log('Got a response from the API'));
}
