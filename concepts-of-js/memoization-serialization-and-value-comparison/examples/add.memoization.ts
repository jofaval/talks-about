function add(a: number, b: number): number {
  return a + b;
}

const memoizedAddCache = new Map<string, number>();

function memoizedAdd(a: number, b: number): number {
  const serializedArguments = [a, b].toString();

  const cachedEntry = memoizedAddCache.get(serializedArguments);
  if (cachedEntry) {
    return cachedEntry;
  }

  console.log("computing...");

  const result = add(a, b);
  memoizedAddCache.set(serializedArguments, result);
  return result;
}
