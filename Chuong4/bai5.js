const m=[5,-10,3,4,8,11,-2]
let s=0;
let dem=0;
for (let i=0;i<m.length;i=i+1)
{
    if (m[i]%2===0)
    { 
        dem=dem+1
        s=s+m[i]
    }
        
}
console.log("so luong cac so chan= " +dem)
console.log("tbc cua cac so chan= " +s/dem)
for (let i=0;i<m.length;i=i+1)
{ if (m[i]===5)
    m[i]=10
}
    
console.log(m)
m.push(10,11,12)
console.log(m)