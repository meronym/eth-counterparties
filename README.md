# eth-counterparties
List Ethereum account counterparties induxed by the transaction graph

### Data sourcing

Using [Alethio's API](https://docs.aleth.io/api) for fetching Ethereum data.

API Key not required, but preferable for higher throughputs.

### Setup

Runs on native Python3, no external libraries required.
Clone the repository and launch the scanner.

### Example

```bash
$ python scan.py 0x6ad1b274fbe64984945d1ec454610332352c3e0b --days=1

Fetching counterparties for 0x6ad1b274fbe64984945d1ec454610332352c3e0b after 2020-03-11 13:58:48.178307 .
  14 counterparties found in 15 transactions
0x86a603372485cb4d5df3449f4e2d891ae067262a
0x9ea766a7057a9c2f8e773fdf01c57702fb81dea4
0x0ab5db21f4b6f487ebb16e823211ab6f1af8f6e9
0x7149a6c7d5d1be456527e2ef88baf8113a5faad2
0x2284a6f6f1bbdc4afd477832c973ce92eb1ddb8e
0xa22c1b5320108c19db53f58241fd64b105562296
0xbba939abd9834c8bf322dddc82c8baaf0659b0f5
0x6fdefc17bfdc39fef6aa13283452d6a35fd02d5f
0x919355b4ce85a9b851ead35fd75e798ec74844b0
0x8224122e6395920bed31aa707ca1e92a5041f297
0xe3efb4f32296a8477610122453ffb37d7312bf64
0x57a88f99a5a44734b9cb889339f2a555fac0fbb4
0x26e4570b92b239dc38eb9b940fcafc8c2edaae56
0x91bad039c6db197afba15640421bf04dd1a5fb1b
Fetching counterparties for 0x86a603372485cb4d5df3449f4e2d891ae067262a after 2020-03-11 13:58:48.178307 .
  1 counterparties found in 1 transactions
Fetching counterparties for 0x9ea766a7057a9c2f8e773fdf01c57702fb81dea4 after 2020-03-11 13:58:48.178307 .
  2 counterparties found in 2 transactions
Fetching counterparties for 0x0ab5db21f4b6f487ebb16e823211ab6f1af8f6e9 after 2020-03-11 13:58:48.178307 .
  2 counterparties found in 2 transactions
Fetching counterparties for 0x7149a6c7d5d1be456527e2ef88baf8113a5faad2 after 2020-03-11 13:58:48.178307 .
  2 counterparties found in 2 transactions
Fetching counterparties for 0x2284a6f6f1bbdc4afd477832c973ce92eb1ddb8e after 2020-03-11 13:58:48.178307 .
  2 counterparties found in 3 transactions
Fetching counterparties for 0xa22c1b5320108c19db53f58241fd64b105562296 after 2020-03-11 13:58:48.178307 .....................
  1656 counterparties found in 2005 transactions
Fetching counterparties for 0xbba939abd9834c8bf322dddc82c8baaf0659b0f5 after 2020-03-11 13:58:48.178307 .
  1 counterparties found in 1 transactions
Fetching counterparties for 0x6fdefc17bfdc39fef6aa13283452d6a35fd02d5f after 2020-03-11 13:58:48.178307 .
  1 counterparties found in 1 transactions
Fetching counterparties for 0x919355b4ce85a9b851ead35fd75e798ec74844b0 after 2020-03-11 13:58:48.178307 .
  1 counterparties found in 1 transactions
Fetching counterparties for 0x8224122e6395920bed31aa707ca1e92a5041f297 after 2020-03-11 13:58:48.178307 .
  2 counterparties found in 2 transactions
Fetching counterparties for 0xe3efb4f32296a8477610122453ffb37d7312bf64 after 2020-03-11 13:58:48.178307 .
  1 counterparties found in 1 transactions
Fetching counterparties for 0x57a88f99a5a44734b9cb889339f2a555fac0fbb4 after 2020-03-11 13:58:48.178307 .
  1 counterparties found in 1 transactions
Fetching counterparties for 0x26e4570b92b239dc38eb9b940fcafc8c2edaae56 after 2020-03-11 13:58:48.178307 .
  2 counterparties found in 2 transactions
Fetching counterparties for 0x91bad039c6db197afba15640421bf04dd1a5fb1b after 2020-03-11 13:58:48.178307 .
  2 counterparties found in 2 transactions
0xcb419bf28ba22b572d2b869c2fedb6cb2f0c17f4
0x4bf5edd75faef666d746f7505cb08484dcfb39e9
0x62354c549e90c34128fdae453d163600f75a5990
0xac15ba93e7f86f3f8d65f93eaefef1afae15d5dc
0xb6c26b66105010fc182da29fca7529c986e24230
0x8d9332d61db725d6ccc7edf6dddd6794b803ee57
0x7e4bf92704338d1901060d97a0d91db625101c9d
0x48896f7c8ff191f7fa16105ea678402d836daaa3
0x5e6e5e2e2f5594931a7c1487fcf4e6b57cb403ad
(... truncated)

```
