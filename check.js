const ORDER=["Red","Blue","Green","Yellow","Peach","White"];
const DAY=86400000, ANCHOR=Date.UTC(2026,4,27), ANCHOR_IDX=5;
const wd=ms=>new Date(ms).getUTCDay();
const isB=ms=>wd(ms)===0||wd(ms)===3;
const pStart=ms=>{let t=ms;while(!isB(t))t-=DAY;return t;};
const nextB=ms=>{let t=ms+DAY;while(!isB(t))t+=DAY;return t;};
function pc(ms){let t=pStart(Date.UTC(2025,0,1)),ps=pStart(ms),c=0;while(t<=ps){c++;t=nextB(t);}return c;}
const BASE=pc(ANCHOR);
function st(ms){const n=((ANCHOR_IDX+(pc(ms)-BASE))%6+6)%6;return ORDER.map((c,i)=>{const a=((n-i)%6+6)%6;return a===0?"NEW":a<=2?"full":a<=4?"50":"75";});}
let out=[];
for(const [y,m,d] of [[2026,5,30],[2026,5,31],[2026,6,3],[2026,1,1],[2026,12,25],[2026,7,15]]){
  out.push(`${y}-${m}-${d} `+st(Date.UTC(y,m-1,d)).map((s,i)=>ORDER[i]+":"+s).join(" "));
}
console.log(out.join("\n"));
