type UseStateResponse<T> = [() => T, (v: T) => void];

(() => {
  const useState = <TValue extends any>(
    initial?: TValue
  ): UseStateResponse<TValue> => {
    const valueHolder = {
      _test: initial,
      get test() {
        return this._test;
      },
      set test(v) {
        this._test = v;
      },
    };

    const getValue = () => valueHolder.test;
    const setValue = (v) => (valueHolder.test = v);

    return [getValue, setValue];
  };

  const [value, setter] = useState(1);
  console.log(value()); // 1
  setter(2);
  console.log(value()); // 2
})();
