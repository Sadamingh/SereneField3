### Non-Relational Database 3 |

![mongodb](../../image/mongodb.png)

#### 1. Cursor Method

**(1) The Definition of Cursor**

In MongoDB, the `find()` method returns a cursor by which we can use to control the output of a query.

**(2) The Definition of Cursor Methods**

The cursor methods are methods used to modify the way that the underlying query is executed.

**(3) Common Cursor Methods**

* Count the returned number of documents

```
db.collection_name.find().count()
```

* Configures the cursor to display results in an easy-to-read format.

```
db.collection_name.find().pretty()
```

* Sort returned documents by the values ascendingly for `field`

```
db.collection_name.find().sort({"field" : 1})
```

* Sort returned documents by the values descendingly for `field`

```
db.collection_name.find().sort({"field" : -1})
```

* Return the first `N` document for the cursor

```
db.collection_name.find().limit(N)
```

**(4) Range Operators**

When we returns a cursor by `find()`, we can restrict the range of the matching values. The syntax should be,

```
db.collection_name.find({field:{range_operator:value}})
```

Where the range operators are,

```
$lt      means less than value
$lte     means less than or equal to value
$gt      means greater than value
$gte     means greater than or equal to value
$eq      means equal to value
$ne      means not equal to value
```

**(5) Logoical Operator**

When we returns a cursor by `find()`, we can also query with the logical combinations of different conditions. 







