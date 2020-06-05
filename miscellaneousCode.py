import graphviz
def gv(s): return graphviz.Source('digraph G{ rankdir="LR"' + s + '; }')
gv(''' "|Ai- Aj| + |i-j|"->"Ai-Aj+i-j"->"(Ai+i)-(Aj+j)"->"1"; 
       "|Ai- Aj| + |i-j|"->"Ai-Aj+j-i"->"(Ai-i)-(Aj-j)"->"2";
       "|Ai- Aj| + |i-j|"->"Aj-Ai+i-j"->"(Ai-j)-(Ai-i)"->"3";
       "|Ai- Aj| + |i-j|"->"Aj-Ai+j-i"->"(Aj+j)-(Ai+i)"->"4"
       ''')
