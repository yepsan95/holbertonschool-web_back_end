export default function getResponseFromAPI() {
  const myPromise = new Promise((resolve, reject) => {
    resolve('Success!');
    reject(new Error('Failure!'));
  });
  return myPromise;
}
