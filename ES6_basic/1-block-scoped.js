export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
	task = false;
	task2 = true;
  }

  return [task, task2];
}
