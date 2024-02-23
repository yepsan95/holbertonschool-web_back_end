export default function uploadPhoto(filename) {
  if (typeof filename !== 'string') throw new Error('filename must be a string');
  return Promise.reject(new Error(`${filename} cannot be processed`));
}
