export default class HolbertonCourse {
  constructor(name, length, students) {
	  this.name = name;
	  this.length = length;
	  this.students = students;
  }
  set name(newValue) {
    if (typeof newValue === 'string') {
      this._name = newValue;
	}
  }
  set length(newValue) {
    if (typeof newValue === 'number') {
      this._length = newValue;
	}
  }
  set students(newValue) {
    if (Array.isArray(newValue)) {
      for (const item of newValue) {
        if (typeof item === 'string') {
          allStrings = true;
		} else {
          allStrings = false;
		  break;
		}
	  }
	  if (allStrings === true) {
        this._students = newValue;
	  }
	}
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
