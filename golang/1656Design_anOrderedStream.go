type OrderedStream struct {
    stream []string
    ptr int
}


func Constructor(n int) OrderedStream {
    return OrderedStream{make([]string, n+1), 1}
}

//https://go.dev/tour/methods/1
//https://go.dev/tour/methods/4
func (this *OrderedStream) Insert(idKey int, value string) []string {
    this.stream[idKey] = value
    start := this.ptr 
    for this.ptr < len(this.stream) && this.stream[this.ptr] != "" {
        this.ptr++
    }
    return this.stream[start:this.ptr]
}


/**
 * Your OrderedStream object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Insert(idKey,value);
 */
