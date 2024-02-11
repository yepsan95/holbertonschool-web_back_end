export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
	allStrings = false;
    if (Array.isArray(students)) {
      for (const item of students) {
        if (typeof item === 'string') {
          allStrings = true;
		} else {
          allStrings = false;
		  break;
		}
	  }
	}
	if (allStrings !== true) throw TypeError('Students must be an array of strings');
    this._name = name;
    this._length = length;
    this._students = students;
  }
  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('Name must be a string');
    this._name = newName;
  }
  set length(newLength) {
    if (typeof newLength !== 'number') throw TypeError('Length must be a number');
    this._length = newLength;
  }
  set students(newStudents) {
	allStrings = false;
    if (Array.isArray(newStudents)) {
      for (const item of newStudents) {
        if (typeof item === 'string') {
          allStrings = true;
		} else {
          allStrings = false;
		  break;
		}
	  }
	}
	if (allStrings !== true) throw TypeError('Students must be an array of strings');
    this._students = newStudents;
  }
  get name() {
    return this._name;
  }
  get length() {
    return this._length;
  }
  get students() {
    return this._students;
  }
}
