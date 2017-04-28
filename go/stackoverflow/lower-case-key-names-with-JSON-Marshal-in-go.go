// http://stackoverflow.com/questions/11693865/lower-case-key-names-with-json-marshal-in-go
// Lower case key names with JSON Marshal in Go

// I wish to use the "encoding/json" package to marshal(排列,整理,编列) a struct declared
// in one of the imported packages of my application.

// Because it is imported, all available (exported) fields in the struct begins with an upper case letter.
// But I wish to have lower case key names.

// It might be a silly little thing, but my coding convertion in Javascript uses lower case keys for object properties.

// Is it possible to get around the problem in some easy way,
// or is the easiest way "just to live with ucfirst keys"?

////////////////////////

// Have a look at the docs for `encoding/json.Marshal`.
// It discusses using struct field tags to determine how the generated json is formatted.

// For example:

type T struct {
    FieldA int      `json:"field_a"`
    FieldB string   `json:"field_b,omitempty"`
}

// This will generate JSON as follows:

{
    "field_a": 1234,
    "field_b": "foobar"
}
