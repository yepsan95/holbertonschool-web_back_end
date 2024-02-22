export default function handleResponseFromAPI(promise) {
  promise.then((result) => {
    console.log('Got a response from the API');
    const resolveObject = {
      status: 200,
	  body: success,
    };
    return resolveObject;
  }).catch((error) => {
    return (new Error());
  });
}
