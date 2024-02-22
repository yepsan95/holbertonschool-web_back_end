export default function handleResponseFromAPI(promise) {
  promise.then(() => {
    console.log('Got a response from the API');
    const resolveObject = {
      status: 200,
      body: 'success',
    };
    return resolveObject;
  }).catch(() => {return (new Error())});
}
