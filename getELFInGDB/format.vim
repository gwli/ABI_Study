function! Hex2addr3(hexstr)
	let k=1024.0
	let m=k*1024
	let g=m*1024
	let t=g*1024
	let temp =0
	if a:hexstr <k
	   let temp = a:hexstr*1 
	   return temp. "B"
	elseif a:hexstr <m
	   let temp=  a:hexstr/k 
	   return  string(temp) . "K"
	elseif a:hexstr <g
	   let temp=  a:hexstr/m 
	   return  string(temp) . "M"
	elseif a:hexstr <t
	   let temp=  a:hexstr/g 
	   return  string(temp) . "G"
	else
	   let temp= a:hexstr/t  
	   return string(temp)  . "T"
	endif

endfunction
g/0x/s#0x[0-9a-z]\{6,16}#\=printf("%s (%4s)",submatch(0),Hex2addr3(submatch(0)))#gc
