export default function getFullResponseFromAPI(success) {
  const myPromise = new Promise((resolve, reject) => {
    if (success) {
      const successObject = {
        'status': 200,
	    'body': 'Success',
      };
	  resolve(successObject);
    } else {
      const errorObject = new Error('The fake API is not working currently');
      reject(errorObject);
    }
  });
}
