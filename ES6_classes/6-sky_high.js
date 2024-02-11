import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    if (typeof (sqft) !== 'number') {
      throw TypeError('sqft must be a number');
    }
    if (typeof (floors) !== 'number') {
      throw TypeError('floors must be a number');
    }
    super(sqft);
    this._floors = floors;
  }

  evacuationWarningMessage() {
    const warningMessage = `Evacuate slowly the ${this.floors} floors`;
    return warningMessage;
  }

  get sqft() {
    return super._sqft;
  }

  get floors() {
    return this._floors;
  }
}
