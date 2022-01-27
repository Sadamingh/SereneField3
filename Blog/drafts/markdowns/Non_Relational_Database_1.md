### Non-Relational Database 1 | MongoDB Installation and NoSQL Introduction

![mongodb](../../image/mongodb.png)

#### 1. Installation

* Install MongoDB in a new environment

```bash
$ conda install mongodb
```

* Choose a file path `<filepath>` for running mongoDB

```bash
$ mongod --dbpath=<filepath>
```

* Run client in another terminal

```bash
$ mongo
```

* Download [Studio3T](https://studio3t.com/download/) IDE for MongoDB

#### 2. NoSQL

**(1) Reasons for Non-Relational Database (aka. NoSQL Database)** 

* **Big data**: volume (EB), variety (unstructured), and velocity (high speed) of data is beyonf the ability of traditional data-processing applications
* **Distributed Computing**: or ptoring and processing big data, we have to scale out instead of scale up
* Open-source
* Schemaless
* Scalable

**(2) JSON Type**

JSON (aka. JavaScript Object Notation) is an open-standard file format that uses human-readable text to transmit data objects consisting of key-value pairs and array data types. They are commonly used for browser-server communication for REST API.

**(3) The Features of NoSQL**

NoSQL (aka. Not Only SQL) generally has the following features,

* Take schemaless data
* Non-relational
* Open-source applications
* Trade off traditional consistency for other properties
* Run on clusters

**(4) Reasons for NoSQL**

* **Impedance mismatch**: relational model doesn't fit in-memory data structure
* **Large volume of data**: easy to manage big data on distributed clusters

**(5) Examples of NoSQL Database**

* Aggregated-oriented NoSQL Database
  * Key-value Database: Redis
  * Document Database: MongoDB
  * Columnar Database (Column family): Hbase
* Relationship-oriented NoSQL Database
  * Graph Database: OrientDB

**(6) Aggregated-oriented NoSQL Database**

Aggregated-oriented means to use a collection of related objects that can be treated as a unit for data manipulation and management. Because relational databases have no concept of aggregrate within their data model, they are so-called aggregate-ignorant.

* An aggregrate is stored together on a node on a cluster
* An aggregrate is a unit of atomic updates
* Aggregated-oriented database use aggregates indexed by key for data lookup
* Aggregated-oriented database don't have ACID transactions

**(7) Relationship-oriented NoSQL Database**

Relationship-oriented database or graph database is a NoSQL database with its relationships and attributes explicitly defined. They are mainly used or data with complex relationships, which forcus on graph traverse more than inserts. Relationship-oriented NoSQL database are designed to run on a single server rather than distributed clusters.

* Nodes: objects
* Edges: relationships