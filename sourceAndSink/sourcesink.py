vertices = int(input())
sources = set()
sink = set()
for source in range(vertices):
   out_going_egdes = list(map(int,input().split()))
   for index in range(vertices):
      if out_going_egdes[index] == 1:
         sources.add(source+1)
         sink.add(index+1)
new_sources = sources-sink
new_sink = sink-sources
for vertex in range(1,vertices+1):
   if vertex not in sink and vertex not in sources:
      new_sources.add(vertex)
      new_sink.add(vertex)
new_sources = sorted(list(new_sources))
new_sink = sorted(list(new_sink))
print(len(new_sources),*new_sources)
print(len(new_sink),*new_sink)

      
      



         