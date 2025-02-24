const fs = require('fs');
const wasmBuffer = fs.readFileSync('hello.wasm');

WebAssembly.instantiate(wasmBuffer).then(wasmModule => {
  wasmModule.instance.exports._main();
});
