function recursiveFactorial(n: number): number {
  if (n <= 1) return 1;
  return recursiveFactorial(n - 1) * n;
}

function factorial(n: number): number {
  if (n <= 1) return 1;

  let accumulative = 1;
  for (let factorialIndex = 2; factorialIndex <= n; factorialIndex++) {
    accumulative *= factorialIndex;
  }

  return accumulative;
}
