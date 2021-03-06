 1. 对程序耗时影响最大的是文件流的开关以及读写次数，经过测试之后发现读写的内容多少对耗时影响不大，所以减少文件流开关和读写的次数可以显著减少耗时（`/src` 中的代码在 oj 上耗时 5212 ms，而且没有开 `-Ofast` ）。所以建议一个储存文件对应一个对象，一个文件只开一个文件流指针（两个文件流指针打开同个文件修改的时候容易出问题），在构造函数里打开，析构函数里关闭。
   
 2. 判断是否到文件流指针 `fio` 是否到文件末可以用 `fio.peek() != EOF`。

 3. `fstream` 文件流指针移动的时候应该用 `seekg()`。因为如果文件流指针访问到文件尾时会导致 `eofbit` 变成 true，此时是没办法进行写操作的，而`seekp()`并不能将`eofbit`重置为 false，只有`seekg()`才可以。 

 4. 空行也算 `Invalid`。

 5. 要注意 `select` 是与登陆状态一一对应的，而不是与用户一一对应的，更不是和用户登陆状态互相独立的，具体可以见鲁棒性的第四个测试点。

 6. B+Tree 会遇到有 key 相同的情况，此时需要多维护最后一个儿子所维护的文件位置，相当于第二个关键字，否则后面要删除的时候找不到要删的那个点在哪里。

 7. 在造 B+Tree 轮子时我没有采用网上博客所讲的先考虑左右借再考虑左右合并，按如下写法会更简便一点，而且常数更小。首先一个点一定至少有两个儿子，否则这个点可以跟父节点合并，所以一个点一定有左兄弟或者右兄弟。如果当前节点的儿子个数小于 `max_size / 2` ，那么他的兄弟一定要么可以跟它合并，要么可以借点给它，那么就直接执行这两个的其中一个就好了，而不是先考虑跟左右借再考虑跟左右合并。
   
 8. B+Tree 调不出来的时候可以试试把 `max_size` 设成 2，这样树的深度会很大，比较好调。
   
 9.  B+Tree 可以单独造数据对拍（比如随机生成1000个字符串插入，然后逐个删除，删除一个之后询问所有剩下的字符串之后再删除下一个），不需要非得使用下发的测试数据来测试，这样会更好调试。
  
 10. **当新建了文件并命名的时候就已经成功了一半。**
   

