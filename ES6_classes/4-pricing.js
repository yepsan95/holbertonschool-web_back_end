import Currency from './3-currency'

export default class Pricing {
  constructor(amount, currency) {
    if (typeof (amount) !== 'number') {
      throw TypeError('Amount must be a number');
    }
    if (!(currency instanceof Currency)) {
      throw TypeError('Currency must be a Currency');
    }
	this._amount = amount;
	this._currency = currency;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof (amount) !== 'number') {
      throw TypeError('Amount must be a number');
    }
    if (typeof (conversionRate) !== 'number') {
      throw TypeError('ConversionRate must be a number');
    }
	const result = amount * conversionRate;
	return result;
  }

  displayFullPrice() {
    const output = `${this._amount} ${this._currency._name} (${this._currency._code})`;
	return output;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  set amount(newAmount) {
    if (typeof (newAmount) !== 'number') {
      throw TypeError('Amount must be a number');
    }
	this._amount = newAmount;
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) {
      throw TypeError('Currency must be a Currency');
  }
	this._currency = newCurrency;
}
