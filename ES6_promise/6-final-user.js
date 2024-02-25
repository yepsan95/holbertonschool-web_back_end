import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, filename) {
  const returnArray = [];

  try {
    const signUp = await signUpUser(firstName, lastName);
    returnArray.push({
      status: 'fulfilled',
      value: signUp,
    });
  } catch (error) {
    returnArray.push({
      status: 'rejected',
      value: error.toString(),
    });
  }

  try {
    const upload = await uploadPhoto(filename);
    returnArray.push({
      status: 'fulfilled',
      value: upload,
    });
  } catch (error) {
    returnArray.push({
      status: 'rejected',
      value: error.toString(),
    });
  }

  return returnArray;
}
