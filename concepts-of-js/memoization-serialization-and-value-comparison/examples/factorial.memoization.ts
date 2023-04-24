function recursiveFactorial(n: number): number {
  if (n <= 1) return 1;
  return recursiveFactorial(n - 1) * n;
}

const memoizedRecursiveFactorialCache = new Map<number, number>();

function memoizedRecursiveFactorial(n: number): number {
  const cachedEntry = memoizedRecursiveFactorialCache.get(n);
  if (cachedEntry) {
    return cachedEntry;
  }

  console.log("computing...");

  const result = recursiveFactorial(n);
  memoizedRecursiveFactorialCache.set(n, result);
  return result;
}

// observe how many times "computing..." gets logged for each new bigger number

function factorial(n: number): number {
  if (n <= 1) return 1;

  let accumulative = 1;
  for (let factorialIndex = 2; factorialIndex <= n; factorialIndex++) {
    accumulative *= factorialIndex;
  }

  return accumulative;
}

const memoizedFactorialCache = new Map<number, number>();

function memoizedFactorial(n: number): number {
  const cachedEntry = memoizedFactorialCache.get(n);
  if (cachedEntry) {
    return cachedEntry;
  }

  console.log("computing...");

  const result = factorial(n);
  memoizedFactorialCache.set(n, result);
  return result;
}
