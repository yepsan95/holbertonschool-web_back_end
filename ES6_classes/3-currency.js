export default class Currency {
  constructor(code, name) {
    if (typeof (code) !== 'string') {
      throw TypeError('Code must be a string');
    }
    if (typeof (name) !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._code = code;
    this._name = name;
  }

  displayFullCurrency() {
    const output = `${this._name} (${this._code})`;
    return output;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(newCode) {
    if (typeof (newCode) !== 'string') {
      throw TypeError('Code must be a string');
    }
    this._code = newCode;
  }

  set name(newName) {
    if (typeof (newName) !== 'string') {
      throw TypeError('Code must be a string');
    }
    this._code = newName;
  }
}
