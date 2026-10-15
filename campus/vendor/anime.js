var Dr=Object.defineProperty;var Pr=(e,t)=>{for(var s in t)Dr(e,s,{get:t[s],enumerable:!0})};var de=typeof window<"u",kt=de?window:null,Xe=de?document:null,A={OBJECT:0,ATTRIBUTE:1,CSS:2,TRANSFORM:3,CSS_VAR:4},y={NUMBER:0,UNIT:1,COLOR:2,COMPLEX:3},B={NONE:0,AUTO:1,FORCE:2},I={replace:0,none:1,blend:2},as=Symbol(),be=Symbol(),ct=Symbol(),He=Symbol(),Bt=Symbol(),g=1e-11,St=1e12,me=1e3,Ct=240,ve="",Vs="var(",Rt=[],$t=(()=>{let e=new Map;return e.set("x","translateX"),e.set("y","translateY"),e.set("z","translateZ"),e})(),ut=["perspective","translateX","translateY","translateZ","rotate","rotateX","rotateY","rotateZ","scale","scaleX","scaleY","scaleZ","skew","skewX","skewY"],Ls=ut.reduce((e,t)=>({...e,[t]:t+"("}),{}),K=()=>{},Ms=e=>e,Us=/\)\s*[-.\d]/,Fs=/(^#([\da-f]{3}){1,2}$)|(^#([\da-f]{4}){1,2}$)/i,ks=/rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)/i,Bs=/rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(-?\d+|-?\d*.\d+)\s*\)/i,$s=/hsl\(\s*(-?\d+|-?\d*.\d+)\s*,\s*(-?\d+|-?\d*.\d+)%\s*,\s*(-?\d+|-?\d*.\d+)%\s*\)/i,qs=/hsla\(\s*(-?\d+|-?\d*.\d+)\s*,\s*(-?\d+|-?\d*.\d+)%\s*,\s*(-?\d+|-?\d*.\d+)%\s*,\s*(-?\d+|-?\d*.\d+)\s*\)/i,ls=/[-+]?\d*\.?\d+(?:e[-+]?\d)?/gi,Xs=/^([-+]?\d*\.?\d+(?:e[-+]?\d+)?)([a-z]+|%)$/i,Hs=/([a-z])([A-Z])/g,zs=/(\*=|\+=|-=)/,Ws=/var\(\s*(--[\w-]+)(?:\s*,\s*([^)]+))?\s*\)/;var ft={id:null,keyframes:null,playbackEase:null,playbackRate:1,frameRate:Ct,loop:0,reversed:!1,alternate:!1,autoplay:!0,persist:!1,duration:me,delay:0,loopDelay:0,ease:"out(2)",composition:I.replace,modifier:Ms,onBegin:K,onBeforeUpdate:K,onUpdate:K,onLoop:K,onPause:K,onComplete:K,onRender:K},At={current:null,root:Xe},v={defaults:ft,precision:4,timeScale:1,tickThreshold:200,editor:null},cs={version:"4.5.0",engine:null};de&&(kt.AnimeJS||(kt.AnimeJS=[]),kt.AnimeJS.push(cs));var us=e=>e.replace(Hs,"$1-$2").toLowerCase(),oe=(e,t)=>e.indexOf(t)===0,Ve=Date.now,ze=Array.isArray,Ge=e=>e&&e.constructor===Object,dt=e=>typeof e=="number"&&!isNaN(e),_e=e=>typeof e=="string",Q=e=>typeof e=="function",_=e=>typeof e>"u",xe=e=>_(e)||e===null,mt=e=>de&&e instanceof SVGElement,fs=e=>Fs.test(e),ds=e=>oe(e,"rgb"),ms=e=>oe(e,"hsl"),Js=e=>fs(e)||(ds(e)||ms(e))&&(e[e.length-1]===")"||!Us.test(e)),Nt=e=>!v.defaults.hasOwnProperty(e),Or=["opacity","rotate","overflow","color"],Ks=(e,t)=>{if(Or.includes(t))return!1;if(e.getAttribute(t)||t in e){if(t==="scale"){let s=e.parentNode;return s&&s.tagName==="filter"}return!0}};var Qe=Math.pow,Et=Math.sqrt,Zs=Math.sin,Gs=Math.cos;var Qs=Math.floor,js=Math.asin;var er=Math.atan2,je=Math.PI,Ys=Math.round,j=(e,t,s)=>e<t?t:e>s?s:e,S=(e,t)=>{if(t<0)return e;if(!t)return Ys(e);let s=10**t;return Ys(e*s)/s};var pt=(e,t,s)=>s===1?t:s===0?e:e+(t-e)*s,et=e=>e===1/0?St:e===-1/0?-St:e,Le=e=>e<=g?g:et(S(e,11)),U=e=>ze(e)?[...e]:e,qt=(e,t)=>{let s={...e};for(let r in t){let n=e[r];s[r]=_(n)?t[r]:n}return s},R=(e,t,s,r="_prev",n="_next")=>{let o=e._head,i=n;for(s&&(o=e._tail,i=r);o;){let a=o[i];t(o),o=a}},Me=(e,t,s="_prev",r="_next")=>{let n=t[s],o=t[r];n?n[r]=o:e._head=o,o?o[s]=n:e._tail=n,t[s]=null,t[r]=null},Te=(e,t,s,r="_prev",n="_next")=>{let o=e._tail;for(;o&&s&&s(o,t);)o=o[r];let i=o?o[n]:e._head;o?o[n]=t:e._head=t,i?i[r]=t:e._tail=t,t[r]=o,t[n]=i};var tr=(e,t,s)=>{let r=e.style.transform;if(r){let n=e[He],o=0,i=r.length,a;for(;o<i;){for(;o<i&&r.charCodeAt(o)===32;)o++;if(o>=i)break;let l=o;for(;o<i&&r.charCodeAt(o)!==40;)o++;if(o>=i)break;let u=r.substring(l,o),f=1,d=o+1,p=-1,x=-1;for(o++;o<i&&f>0;){let D=r.charCodeAt(o);D===40?f++:D===41?f--:D===44&&f===1&&(p===-1?p=o:x===-1&&(x=o)),o++}let T=o-1;u==="translate"||u==="translate3d"?(p===-1?n.translateX=r.substring(d,T).trim():(n.translateX=r.substring(d,p).trim(),x===-1?n.translateY=r.substring(p+1,T).trim():(n.translateY=r.substring(p+1,x).trim(),n.translateZ=r.substring(x+1,T).trim())),a=r.substring(d,T)):u==="scale"||u==="scale3d"?p===-1?n.scale=r.substring(d,T).trim():(n.scaleX=r.substring(d,p).trim(),x===-1?n.scaleY=r.substring(p+1,T).trim():(n.scaleY=r.substring(p+1,x).trim(),n.scaleZ=r.substring(x+1,T).trim())):n[u]=r.substring(d,T)}if(t==="translate3d"&&a)return s&&(s[t]=a),a;let c=n[t];if(!_(c))return s&&(s[t]=c),c}return t==="translate3d"?"0px, 0px, 0px":t==="rotate3d"?"0, 0, 0, 0deg":oe(t,"scale")?"1":oe(t,"rotate")||oe(t,"skew")?"0deg":"0px"},Xt=e=>{let t=ve;for(let s=0,r=ut.length;s<r;s++){let n=ut[s],o=e[n];if(o!==void 0){if(n==="translateX"){let i=e.translateY;if(i!==void 0){let a=e.translateZ;a!==void 0?(t+=`translate3d(${o},${i},${a}) `,s+=2):(t+=`translate(${o},${i}) `,s+=1);continue}}if(n==="scaleX"&&e.scale===void 0){let i=e.scaleY;if(i!==void 0){let a=e.scaleZ;a!==void 0?(t+=`scale3d(${o},${i},${a}) `,s+=2):(t+=`scale(${o},${i}) `,s+=1);continue}}t+=`${Ls[n]}${o}) `}n==="rotateZ"&&e.rotate3d!==void 0&&(t+=`rotate3d(${e.rotate3d}) `)}return e.matrix!==void 0&&(t+=`matrix(${e.matrix}) `),e.matrix3d!==void 0&&(t+=`matrix3d(${e.matrix3d}) `),t};var ps=[];function Ht(e,t){if(!e)return null;let s=ps.length;e:for(let r=0;r<s;r++){let n=ps[r];if(n.detect&&!n.detect(e))continue;let o=n.targetAdapters;for(let i=0,a=o.length;i<a;i++){let c=o[i];if(c.detect(e)){let l=c.props[t];if(l&&(!l.gate||l.gate(e)))return l;break e}}}for(let r=0;r<s;r++){let n=ps[r];if(n.detect&&!n.detect(e))continue;let o=n.propertyResolvers;for(let i=0,a=o.length;i<a;i++){let c=o[i](e,t);if(c)return c}}return null}var wr=e=>{let t=ks.exec(e)||Bs.exec(e),s=_(t[4])?1:+t[4];return[+t[1],+t[2],+t[3],s]},Ir=e=>{let t=e.length,s=t===4||t===5;return[+("0x"+e[1]+e[s?1:2]),+("0x"+e[s?2:3]+e[s?2:4]),+("0x"+e[s?3:5]+e[s?3:6]),t===5||t===9?+(+("0x"+e[s?4:7]+e[s?4:8])/255).toFixed(3):1]},hs=(e,t,s)=>(s<0&&(s+=1),s>1&&(s-=1),s<1/6?e+(t-e)*6*s:s<1/2?t:s<2/3?e+(t-e)*(2/3-s)*6:e),Vr=e=>{let t=$s.exec(e)||qs.exec(e),s=+t[1]/360,r=+t[2]/100,n=+t[3]/100,o=_(t[4])?1:+t[4],i,a,c;if(r===0)i=a=c=n;else{let l=n<.5?n*(1+r):n+r-n*r,u=2*n-l;i=S(hs(u,l,s+1/3)*255,0),a=S(hs(u,l,s)*255,0),c=S(hs(u,l,s-1/3)*255,0)}return[i,a,c,o]},sr=e=>ds(e)?wr(e):fs(e)?Ir(e):ms(e)?Vr(e):[0,0,0,1];var V=(e,t)=>_(e)?t:e,rr=(e,t)=>{let s=e.match(Ws),r=t[be]?t:document.documentElement,n=getComputedStyle(r)?.getPropertyValue(s[1]);return(!n||n.trim()===ve)&&s[2]&&(n=s[2].trim()),n||0},Se=(e,t,s,r,n,o)=>{if(Q(e)){if(!n){let a=e(t,s,r,o);return isNaN(+a)?a||0:+a}let i=()=>{let a=e(t,s,r,o);return isNaN(+a)?a||0:+a};return n.func=i,i()}if(_e(e)&&oe(e,Vs)){if(!n)return rr(e,t);let i=()=>rr(e,t);return n.func=i,i()}return e},_s=(e,t)=>e[be]?e[ct]&&Ks(e,t)?A.ATTRIBUTE:ut.includes(t)||$t.get(t)?A.TRANSFORM:oe(t,"--")?A.CSS_VAR:t in e.style?A.CSS:t in e?A.OBJECT:A.ATTRIBUTE:A.OBJECT,nr=(e,t,s)=>{let r=e.style[t];r&&s&&(s[t]=r);let n=r||getComputedStyle(e[Bt]||e).getPropertyValue(t);return n==="auto"?"0":n},ht=(e,t,s,r)=>{let n=_(s)?_s(e,t):s,o=Ht(e,t);if(o){let i=o.get(e);return i&&r&&(r[t]=i),i??0}if(n===A.OBJECT){let i=e[t];return i&&r&&(r[t]=i),i||0}if(n===A.ATTRIBUTE){let i=e.getAttribute(t);return i&&r&&(r[t]=i),i}return n===A.TRANSFORM?tr(e,t,r):n===A.CSS_VAR?nr(e,t,r).trimStart():nr(e,t,r)},_t=(e,t,s)=>s==="-"?e-t:s==="+"?e+t:e*t,zt=()=>({t:y.NUMBER,n:0,u:null,o:null,d:null,s:null}),ee=(e,t)=>{if(t.t=y.NUMBER,t.n=0,t.u=null,t.o=null,t.d=null,t.s=null,!e)return t;let s=+e;if(!isNaN(s))return t.n=s,t;let r=e;r[1]==="="&&(t.o=r[0],r=r.slice(2));let n=r.includes(" ")?!1:Xs.exec(r);if(n)return t.t=y.UNIT,t.n=+n[1],t.u=n[2],t;if(t.o)return t.n=+r,t;if(Js(r))return t.t=y.COLOR,t.d=sr(r),t;{let o=r.match(ls);return t.t=y.COMPLEX,t.d=o?o.map(Number):[],t.s=r.split(ls)||[],t}},Ts=(e,t)=>(t.t=e._valueType,t.n=e._toNumber,t.u=e._unit,t.o=null,t.d=U(e._toNumbers),t.s=U(e._strings),t),ie=zt(),Wt=(e,t,s)=>{let r=e._modifier,n=e._fromNumbers,o=e._toNumbers,i=e._strings,a=i[0];for(let c=0,l=o.length;c<l;c++){let u=r(S(pt(n[c],o[c],t),s)),f=i[c+1];a+=`${f?u+f:u}`,e._numbers[c]=u}return a};var Dt=(e,t,s,r,n)=>{let o=e.parent,i=e.duration,a=e.completed,c=e.iterationDuration,l=e.iterationCount,u=e._currentIteration,f=e._loopDelay,d=e._reversed,p=e._alternate,x=e._hasChildren,T=e._delay,D=e._currentTime,F=T+c,O=t-T,L=j(D,-T,i),w=j(O,-T,i),q=O-D,P=w>0,pe=w>=i,Ae=i<=g,Ne=n===B.FORCE,Ee=0,ke=O,De=0;if(l>1){let Be=c+(pe?0:f),W=~~(w/Be);e._currentIteration=j(W,0,l),pe&&e._currentIteration--,Ee=e._currentIteration%2,ke=w-W*Be||0}let st=d^(p&&Ee),rt=e._ease,M=pe?st?0:i:st?c-ke:ke;rt&&(M=c*rt(M/c)||0);let X=(o?o.backwards:O<D)?!st:!!st;if(e._currentTime=O,e._iterationTime=M,e.backwards=X,P&&!e.began?(e.began=!0,!s&&!(o&&(X||!o.began))&&e.onBegin(e)):O<=0&&(e.began=!1),!s&&!x&&P&&e._currentIteration!==u&&e.onLoop(e),Ne||n===B.AUTO&&(t>=(o&&T>0?0:T)&&t<=F||t<=T&&L>T||t>=F&&L!==i)||M>=F&&L!==i||M<=T&&L>0&&!pe||t<=L&&L===i&&a||pe&&!a&&Ae){if(P&&(e.computeDeltaTime(L),s||e.onBeforeUpdate(e)),!x){let Be=Ne||(X?q*-1:q)>=v.tickThreshold,W=S(e._offset+(o?o._offset:0)+T+M,12),m=e._head,N,Z,ae,Je,nt=0;for(;m;){let le=m._composition,Y=m._currentTime,$e=m._changeDuration,ce=m._absoluteStartTime+m._changeDuration,E=m._nextRep,G=m._prevRep,Pe=le!==I.none,te=G?G._absoluteStartTime+G._changeDuration:0,ge=G&&G.parent!==m.parent,Oe=!E||E._isOverridden?ce:E.parent===m.parent?ce+E._delay:E._absoluteStartTime<E._absoluteUpdateStartTime?E._absoluteStartTime:E._absoluteUpdateStartTime;if((Be||(Y!==$e||W<=Oe||G&&!ge&&(!E||E.parent!==m.parent))&&(Y!==0||W>=m._absoluteStartTime||ge&&!m._hasFromValue&&!G._isOverridden&&W>=te||E&&!E._isOverridden&&E.parent===m.parent&&E._currentTime!==0&&M<E._startTime))&&(!G||ge||M>=m._startTime)&&(!Pe||!m._isOverridden&&(!m._isOverlapped||W<=ce)&&(!E||E._isOverridden||W<=Oe)&&(!G||G._isOverridden||(ge?W>=m._absoluteStartTime||!m._hasFromValue&&W>=te:W>=te+m._delay)))){let Ke=m._currentTime=j(M-m._startTime,0,$e),H=m._ease(Ke/m._updateDuration),se=m._modifier,ue=m._valueType,re=m._tweenType,ot=re===A.OBJECT,he=ue===y.NUMBER,we=he&&ot||H===0||H===1?-1:v.precision,k,Ie;if(he)k=Ie=se(S(pt(m._fromNumber,m._toNumber,H),we));else if(ue===y.UNIT)Ie=se(S(pt(m._fromNumber,m._toNumber,H),we)),k=`${Ie}${m._unit}`;else if(ue===y.COLOR){let z=m._numbers,qe=m._fromNumbers,ye=m._toNumbers,it=1-H,Mt=qe[0],Ut=qe[1],at=qe[2],lt=ye[0],Ze=ye[1],vt=ye[2];z[0]=se(Math.sqrt(Mt*Mt*it+lt*lt*H)),z[1]=se(Math.sqrt(Ut*Ut*it+Ze*Ze*H)),z[2]=se(Math.sqrt(at*at*it+vt*vt*H)),z[3]=se(pt(qe[3],ye[3],H)),(!m._setter||r)&&(k=`rgba(${S(z[0],0)},${S(z[1],0)},${S(z[2],0)},${z[3]})`)}else ue===y.COMPLEX&&(k=Wt(m,H,we));if(Pe&&(m._number=Ie),!r&&le!==I.blend){let z=m.property;N=m.target,m._setter?m._setter(N,Ie,m):ot?N[z]=k:re===A.ATTRIBUTE?N.setAttribute(z,k):(Z=N.style,re===A.TRANSFORM?(N!==ae&&(ae=N,Je=N[He]),Je[z]=k,nt=1):re===A.CSS?Z[z]=k:re===A.CSS_VAR&&Z.setProperty(z,k)),P&&(De=1)}else m._value=k}else Y&&G&&!ge&&M<m._startTime&&(m._currentTime=0);nt&&m._renderTransforms&&(Z.transform=Xt(Je),nt=0),m=m._next}!s&&De&&e.onRender(e)}!s&&P&&e.onUpdate(e)}return o&&Ae?!s&&(o.began&&!X&&O>0&&!a||X&&O<=g&&a)&&(e.onComplete(e),e.completed=!X):P&&pe?l===1/0?e._startTime+=e.duration:e._currentIteration>=l-1&&(e.paused=!0,!a&&!x&&(e.completed=!0,!s&&!(o&&(X||!o.began))&&(e.onComplete(e),e._resolve(e)))):e.completed=!1,De},Ce=(e,t,s,r,n)=>{let o=e._currentIteration;if(Dt(e,t,s,r,n),e._hasChildren){let i=e,a=i.backwards,c=r?t:i._iterationTime,l=Ve(),u=0,f=!0;if(!r&&i._currentIteration!==o){let d=i.iterationDuration;R(i,p=>{if(!a)!p.completed&&!p.backwards&&p._currentTime<p.iterationDuration&&Dt(p,d,s,1,B.FORCE),p.began=!1,p.completed=!1;else{let x=p.duration,T=p._offset+p._delay,D=T+x;!s&&x<=g&&(!T||D===d)&&p.onComplete(p)}}),s||i.onLoop(i)}R(i,d=>{let p=S((c-d._offset)*d._speed,12);if(a&&p>d._delay+d.duration)return;let x=d._fps<i._fps?d.requestTick(l):n;u+=Dt(d,p,s,r,x),!d.completed&&f&&(f=!1)},a),!s&&u&&i.onRender(i),(f||a)&&i._currentTime>=i.duration&&(i.paused=!0,i.completed||(i.completed=!0,s||(i.onComplete(i),i._resolve(i))))}};var or={},Yt=(e,t,s)=>{if(s===A.TRANSFORM){let r=$t.get(e);return r||e}else if(s===A.CSS||s===A.ATTRIBUTE&&mt(t)&&e in t.style){let r=or[e];if(r)return r;{let n=e&&us(e);return or[e]=n,n}}else return e},Pt=(e,t=!1)=>{if(e._hasChildren)R(e,s=>Pt(s,t),!0);else{let s=e;s.pause(),R(s,r=>{let n=r.property,o=r.target,i=r._tweenType,a=r._inlineValue,c=xe(a)||a===ve;if(r._setter){if(!t&&!c){if(ee(a,ie),ie.d){let l=ie.d,u=r._numbers;for(let f=0,d=l.length;f<d;f++)u[f]=l[f]}else r._number=ie.n;r._setter(r.target,r._number,r)}}else if(i===A.OBJECT)!t&&!c&&(o[n]=a);else if(o[be])if(i===A.ATTRIBUTE)t||(c?o.removeAttribute(n):o.setAttribute(n,a));else{let l=o.style;if(i===A.TRANSFORM){let u=o[He];c?delete u[n]:u[n]=a,r._renderTransforms&&(Object.keys(u).length?l.transform=Xt(u):l.removeProperty("transform"))}else c?l.removeProperty(us(n)):l[n]=a}o[be]&&s._tail===r&&s.targets.forEach(l=>{l.getAttribute&&l.getAttribute("style")===ve&&l.removeAttribute("style")})})}return e};var Tt=class{constructor(t=0){this.deltaTime=0,this._currentTime=t,this._lastTickTime=t,this._startTime=t,this._lastTime=t,this._frameDuration=me/Ct,this._fps=Ct,this._speed=1,this._hasChildren=!1,this._head=null,this._tail=null}get fps(){return this._fps}set fps(t){let s=+t,r=s<g?g:s,n=me/r;r>ft.frameRate&&(ft.frameRate=r),this._fps=r,this._frameDuration=n}get speed(){return this._speed}set speed(t){let s=+t;this._speed=s<g?g:s}requestTick(t){let s=this._frameDuration,r=t-this._lastTickTime,n=s*.25,o=n<4?n:4;return r+o<s?B.NONE:(this._lastTickTime=r>=s?t-r%s:t,B.AUTO)}computeDeltaTime(t){let s=t-this._lastTime;return this.deltaTime=s,this._lastTime=t,s}};var Ue={animation:null,update:K},ir=e=>{let t=Ue.animation;return t||(t={duration:g,computeDeltaTime:K,_offset:0,_delay:0,_head:null,_tail:null},Ue.animation=t,Ue.update=()=>{e.forEach(s=>{for(let r in s){let n=s[r],o=n._head;if(o){let i=o._valueType,a=i===y.COMPLEX||i===y.COLOR?U(o._fromNumbers):null,c=o._fromNumber,l=n._tail;for(;l&&l!==o;){if(a)for(let u=0,f=l._numbers.length;u<f;u++)a[u]+=l._numbers[u];else c+=l._number;l=l._prevAdd}o._toNumber=c,o._toNumbers=a}}}),Dt(t,1,1,0,B.FORCE)}),t};var ar=de?requestAnimationFrame:setImmediate,Lr=de?cancelAnimationFrame:clearImmediate,gs=class extends Tt{constructor(t){super(t),this.useDefaultMainLoop=!0,this.pauseOnDocumentHidden=!0,this.defaults=ft,this.paused=!0,this.reqId=0}update(){let t=this._currentTime=Ve();if(this.requestTick(t)){this.computeDeltaTime(t);let s=this._speed,r=this._fps,n=this._head;for(;n;){let o=n._next;n.paused?(Me(this,n),this._hasChildren=!!this._tail,n._running=!1,n.completed&&!n._cancelled&&n.cancel()):Ce(n,(t-n._startTime)*n._speed*s,0,0,n._fps<r?n.requestTick(t):B.AUTO),n=o}Ue.update()}}wake(){return this.useDefaultMainLoop&&!this.reqId&&(this.requestTick(Ve()),this.reqId=ar(lr)),this}pause(){if(this.reqId)return this.paused=!0,Mr()}resume(){if(this.paused)return this.paused=!1,R(this,t=>t.resetTime()),this.wake()}get speed(){return this._speed*(v.timeScale===1?1:me)}set speed(t){let s=t*v.timeScale;this._speed!==s&&(this._speed=s,R(this,r=>r.speed=r._speed))}get timeUnit(){return v.timeScale===1?"ms":"s"}set timeUnit(t){let r=t==="s",n=r?.001:1;if(v.timeScale!==n){v.timeScale=n,v.tickThreshold=200*n;let o=r?.001:me;this.defaults.duration*=o,this._speed*=o}}get precision(){return v.precision}set precision(t){v.precision=t}},$=(()=>{let e=new gs(Ve());return de&&(cs.engine=e,Xe.addEventListener("visibilitychange",()=>{e.pauseOnDocumentHidden&&(Xe.hidden?e.pause():e.resume())})),e})(),lr=()=>{$._head?($.reqId=ar(lr),$.update()):$.reqId=0},Mr=()=>(Lr($.reqId),$.reqId=0,$);var Jt={_rep:new WeakMap,_add:new Map},wt=(e,t,s="_rep")=>{let r=Jt[s],n=r.get(e);return n||(n={},r.set(e,n)),n[t]?n[t]:n[t]={_head:null,_tail:null}},Ur=(e,t)=>e._isOverridden||e._absoluteStartTime>t._absoluteStartTime,Ot=e=>{e._isOverlapped=1,e._isOverridden=1,e._changeDuration=g,e._currentTime=g},Kt=(e,t)=>{let s=e._composition;if(s===I.replace){let r=e._absoluteStartTime;Te(t,e,Ur,"_prevRep","_nextRep");let n=e._prevRep;if(n){let o=n.parent,i=n._absoluteEndTime;if(e.parent.id!==o.id&&o.iterationCount>1&&i+(o.duration-o.iterationDuration)>r){Ot(n);let l=n._prevRep;for(;l&&l.parent.id===o.id;)Ot(l),l=l._prevRep}let a=e._absoluteUpdateStartTime;if(i>a){let l=n._startTime,u=i-(l+n._updateDuration),f=S(a-u-l,12);n._changeDuration=f,n._currentTime=f,n._isOverlapped=1,f<g&&Ot(n)}let c=e.parent.parent;if(!c||c!==o.parent){let l=!0;if(R(o,u=>{u._isOverlapped||(l=!1)}),l){let u=o.parent;if(u){let f=!0;R(u,d=>{d!==o&&R(d,p=>{p._isOverlapped||(f=!1)})}),f&&u.cancel()}else o.cancel()}}}}else if(s===I.blend){let r=wt(e.target,e.property,"_add"),n=ir(Jt._add),o=r._head;o||(o={...e},o._composition=I.replace,o._updateDuration=g,o._startTime=0,o._numbers=U(e._fromNumbers),o._number=0,o._next=null,o._prev=null,Te(r,o),Te(n,o));let i=e._toNumber;if(e._fromNumber=o._fromNumber-i,e._toNumber=0,e._numbers=U(e._fromNumbers),e._number=0,o._fromNumber=i,e._toNumbers.length){let a=U(e._toNumbers);a.forEach((c,l)=>{e._fromNumbers[l]=o._fromNumbers[l]-c,e._toNumbers[l]=0}),o._fromNumbers=a}Te(r,e,null,"_prevAdd","_nextAdd")}return e},ys=e=>{let t=e._composition;if(t!==I.none){let s=e.target,r=e.property,i=Jt._rep.get(s)[r];if(Me(i,e,"_prevRep","_nextRep"),t===I.blend){let a=Jt._add,c=a.get(s);if(!c)return;let l=c[r],u=Ue.animation;Me(l,e,"_prevAdd","_nextAdd");let f=l._head;if(f&&f===l._tail){Me(l,f,"_prevAdd","_nextAdd"),Me(u,f);let d=!0;for(let p in c)if(c[p]._head){d=!1;break}d&&a.delete(s)}}}return e},cr=(e,t,s)=>{let r=!1;return R(t,n=>{let o=n.target;if(e.includes(o)){let i=n.property,a=n._tweenType,c=Yt(s,o,a);(!c||c&&c===i)&&(n.parent._tail===n&&n._tweenType===A.TRANSFORM&&n._prev&&n._prev._tweenType===A.TRANSFORM&&(n._prev._renderTransforms=1),Me(t,n),ys(n),r=!0)}},!0),r},bs=(e,t,s)=>{let r=t||$,n;if(r._hasChildren){let o=0;R(r,i=>{if(!i._hasChildren)if(n=cr(e,i,s),n&&!i._head)i.cancel(),Me(r,i);else{let c=i._offset+i._delay+i.duration;c>o&&(o=c)}i._head?bs(e,i,s):i._hasChildren=!1},!0),_(r.iterationDuration)||(r.iterationDuration=o)}else n=cr(e,r,s);n&&!r._head&&(r._hasChildren=!1,r.cancel&&r.cancel())};var ur=e=>(e.paused=!0,e.began=!1,e.completed=!1,e),vs=e=>(e._cancelled&&(e._hasChildren?R(e,vs):R(e,t=>{t._composition!==I.none&&Kt(t,wt(t.target,t.property))}),e._cancelled=0),e),fr=0,Fr=(e,t)=>e._priority>t._priority,tt=class extends Tt{constructor(t={},s=null,r=0){super(0),++fr;let{id:n,delay:o,duration:i,reversed:a,alternate:c,loop:l,loopDelay:u,autoplay:f,frameRate:d,playbackRate:p,priority:x,onComplete:T,onLoop:D,onPause:F,onBegin:O,onBeforeUpdate:L,onUpdate:w}=t;At.current&&At.current.register(this);let q=s?0:$._lastTickTime,P=s?s.defaults:v.defaults,pe=Q(o)||_(o)?P.delay:+o,Ae=Q(i)||_(i)?1/0:+i,Ne=V(l,P.loop),Ee=V(u,P.loopDelay),ke=Ne===!0||Ne===1/0||Ne<0?1/0:Ne+1,De=0;s?De=r:($.reqId||$.requestTick(Ve()),De=($._lastTickTime-$._startTime)*v.timeScale),this.id=_(n)?fr:n,this.parent=s,this.duration=et((Ae+Ee)*ke-Ee)||g,this.backwards=!1,this.paused=!0,this.began=!1,this.completed=!1,this.onBegin=O||P.onBegin,this.onBeforeUpdate=L||P.onBeforeUpdate,this.onUpdate=w||P.onUpdate,this.onLoop=D||P.onLoop,this.onPause=F||P.onPause,this.onComplete=T||P.onComplete,this.iterationDuration=Ae,this.iterationCount=ke,this._autoplay=s?!1:V(f,P.autoplay),this._offset=De,this._delay=pe,this._loopDelay=Ee,this._iterationTime=0,this._currentIteration=0,this._resolve=K,this._running=!1,this._reversed=+V(a,P.reversed),this._reverse=this._reversed,this._cancelled=0,this._alternate=V(c,P.alternate),this._prev=null,this._next=null,this._lastTickTime=q,this._startTime=q,this._lastTime=q,this._fps=V(d,P.frameRate),this._speed=V(p,P.playbackRate),this._priority=+V(x,1)}get cancelled(){return!!this._cancelled}set cancelled(t){t?this.cancel():this.reset(!0).play()}get currentTime(){return j(S(this._currentTime,v.precision),-this._delay,this.duration)}set currentTime(t){let s=this.paused;this.pause().seek(+t),s||this.resume()}get iterationCurrentTime(){return j(S(this._iterationTime,v.precision),0,this.iterationDuration)}set iterationCurrentTime(t){this.currentTime=this.iterationDuration*this._currentIteration+t}get progress(){return j(S(this._currentTime/this.duration,10),0,1)}set progress(t){this.currentTime=this.duration*t}get iterationProgress(){return j(S(this._iterationTime/this.iterationDuration,10),0,1)}set iterationProgress(t){let s=this.iterationDuration;this.currentTime=s*this._currentIteration+s*t}get currentIteration(){return this._currentIteration}set currentIteration(t){this.currentTime=this.iterationDuration*j(+t,0,this.iterationCount-1)}get reversed(){return!!this._reversed}set reversed(t){t?this.reverse():this.play()}get speed(){return super.speed}set speed(t){super.speed=t,this.resetTime()}reset(t=!1){return vs(this),this._reversed&&!this._reverse&&(this.reversed=!1),this._iterationTime=this.iterationDuration,Ce(this,0,1,~~t,B.FORCE),ur(this),this._hasChildren&&R(this,ur),this}init(t=!1){this.fps=this._fps,this.speed=this._speed,!t&&this._hasChildren&&Ce(this,this.duration,1,~~t,B.FORCE),this.reset(t);let s=this._autoplay;return s===!0?this.resume():s&&!_(s.linked)&&s.link(this),this}resetTime(){let t=1/(this._speed*$._speed);return this._startTime=Ve()-(this._currentTime+this._delay)*t,this}pause(){return this.paused?this:(this.paused=!0,this.onPause(this),this)}resume(){return this.paused?(this.paused=!1,this.duration<=g&&!this._hasChildren?Ce(this,g,0,0,B.FORCE):(this._running||(Te($,this,Fr),$._hasChildren=!0,this._running=!0),this.resetTime(),this._startTime-=12,$.wake()),this):this}restart(){return this.reset().resume()}seek(t,s=0,r=0){vs(this),this.completed=!1;let n=this.paused;return this.paused=!0,Ce(this,t+this._delay,~~s,~~r,B.AUTO),n?this:this.resume()}alternate(){let t=this._reversed,s=this.iterationCount,r=this.iterationDuration,n=s===1/0?Qs(St/r):s;return this._reversed=+(this._alternate&&!(n%2)?t:!t),s===1/0?this.iterationProgress=this._reversed?1-this.iterationProgress:this.iterationProgress:this.seek(r*n-this._currentTime),this.resetTime(),this}play(){return this._reversed&&this.alternate(),this.resume()}reverse(){return this._reversed||this.alternate(),this.resume()}cancel(){return this._hasChildren?R(this,t=>t.cancel(),!0):R(this,ys),this._cancelled=1,this.pause()}stretch(t){let s=this.duration,r=Le(t);if(s===r)return this;let n=t/s,o=t<=g;return this.duration=o?g:r,this.iterationDuration=o?g:Le(this.iterationDuration*n),this._offset*=n,this._delay*=n,this._loopDelay*=n,this}revert(){Ce(this,0,1,0,B.AUTO);let t=this._autoplay;return t&&t.linked&&t.linked===this&&t.revert(),this.cancel()}complete(t=0){return this.seek(this.duration,t).cancel()}then(t=K){let s=this.then,r=()=>{this.then=null,t(this),this.then=s,this._resolve=K};return new Promise(n=>(this._resolve=()=>n(r()),this.completed&&this._resolve(),this))}};function dr(e){let t=_e(e)?At.root.querySelectorAll(e):e;if(t instanceof NodeList||t instanceof HTMLCollection)return t}function We(e){if(xe(e))return[];if(!de)return ze(e)&&e.flat(1/0)||[e];if(ze(e)){let s=e.flat(1/0),r=[];for(let n=0,o=s.length;n<o;n++){let i=s[n];if(!xe(i)){let a=dr(i);if(a)for(let c=0,l=a.length;c<l;c++){let u=a[c];if(!xe(u)){let f=!1;for(let d=0,p=r.length;d<p;d++)if(r[d]===u){f=!0;break}f||r.push(u)}}else{let c=!1;for(let l=0,u=r.length;l<u;l++)if(r[l]===i){c=!0;break}c||r.push(i)}}}return r}let t=dr(e);return t?Array.from(t):[e]}function mr(e){let t=We(e),s=t.length;for(let r=0;r<s;r++){let n=t[r];if(!n[as]){n[as]=!0;let o=mt(n);(n.nodeType||o)&&(n[be]=!0,n[ct]=o,n[He]={})}}return t}var xs={deg:1,rad:180/je,turn:360},pr={},Ss=(e,t,s,r=!1)=>{let n=t.u,o=t.n;if(t.t===y.UNIT&&n===s)return t;let i=o+n+s,a=pr[i];if(!_(a)&&!r)t.n=a;else{let c;if(n in xs)c=o*xs[n]/xs[s];else{let u=e.cloneNode(),f=e.parentNode,d=f&&f!==Xe?f:Xe.body;d.appendChild(u);let p=u.style;p.width=100+n;let x=u.offsetWidth||100;p.width=100+s;let T=u.offsetWidth||100,D=x/T;d.removeChild(u),c=D*o}t.n=c,pr[i]=c}return t.t,y.UNIT,t.u=s,t};var Fe=e=>e;var It=(e=1.68)=>t=>Qe(t,+e),Rs={in:e=>t=>e(t),out:e=>t=>1-e(1-t),inOut:e=>t=>t<.5?e(t*2)/2:1-e(t*-2+2)/2,outIn:e=>t=>t<.5?(1-e(1-t*2))/2:(e(t*2-1)+1)/2},kr=je/2,hr=je*2,_r={[ve]:It,Quad:It(2),Cubic:It(3),Quart:It(4),Quint:It(5),Sine:e=>1-Gs(e*kr),Circ:e=>1-Et(1-e*e),Expo:e=>e?Qe(2,10*e-10):0,Bounce:e=>{let t,s=4;for(;e<((t=Qe(2,--s))-1)/11;);return 1/Qe(4,3-s)-7.5625*Qe((t*3-2)/22-e,2)},Back:(e=1.7)=>t=>(+e+1)*t*t*t-+e*t*t,Elastic:(e=1,t=.3)=>{let s=j(+e,1,10),r=j(+t,g,2),n=r/hr*js(1/s),o=hr/r;return i=>i===0||i===1?i:-s*Qe(2,-10*(1-i))*Zs((1-i-n)*o)}},Cs=(()=>{let e={linear:Fe,none:Fe};for(let t in Rs)for(let s in _r){let r=_r[s],n=Rs[t];e[t+s]=s===ve||s==="Back"||s==="Elastic"?(o,i)=>n(r(o,i)):n(r)}return e})(),Zt={linear:Fe,none:Fe},Br=e=>{if(Zt[e])return Zt[e];if(e.indexOf("(")<=-1){let s=Rs[e]||e.includes("Back")||e.includes("Elastic")?Cs[e]():Cs[e];return s?Zt[e]=s:Fe}else{let t=e.slice(0,-1).split("("),s=Cs[t[0]];return s?Zt[e]=s(...t[1].split(",")):Fe}},Tr=["steps(","irregular(","linear(","cubicBezier("],Vt=e=>{if(_e(e)){for(let s=0,r=Tr.length;s<r;s++)if(oe(e,Tr[s]))return console.warn(`String syntax for \`ease: "${e}"\` has been removed from the core and replaced by importing and passing the easing function directly: \`ease: ${e}\``),Fe}return Q(e)?e:_e(e)?Br(e):Fe};var h=zt(),b=zt(),gt={},Gt={func:null},Qt={func:null},jt=[null],yt=[null,null],es={to:null},$r=0,gr=0,Ye,Re,qr=(e,t)=>{let s={};if(ze(e)){let r=[].concat(...e.map(n=>Object.keys(n))).filter(Nt);for(let n=0,o=r.length;n<o;n++){let i=r[n],a=e.map(c=>{let l={};for(let u in c){let f=c[u];Nt(u)?u===i&&(l.to=f):l[u]=f}return l});s[i]=a}}else{let r=V(t.duration,v.defaults.duration);Object.keys(e).map(o=>({o:parseFloat(o)/100,p:e[o]})).sort((o,i)=>o.o-i.o).forEach(o=>{let i=o.o,a=o.p;for(let c in a)if(Nt(c)){let l=s[c];l||(l=s[c]=[]);let u=i*r,f=l.length,d=l[f-1],p={to:a[c]},x=0;for(let T=0;T<f;T++)x+=l[T].duration;f===1&&(p.from=d.to),a.ease&&(p.ease=a.ease),p.duration=u-(f?x:0),l.push(p)}return o});for(let o in s){let i=s[o],a;for(let c=0,l=i.length;c<l;c++){let u=i[c],f=u.ease;u.ease=a||void 0,a=f}i[0].duration||i.shift()}}return s},bt=class extends tt{constructor(t,s,r,n,o=!1,i=0,a){super(s,r,n),this._head,this._tail,++gr;let c=mr(t),l=c.length,u=s.keyframes,f=u?qt(qr(u,s),s):s,{id:d,delay:p,duration:x,ease:T,playbackEase:D,modifier:F,composition:O,onRender:L}=f,w=r?r.defaults:v.defaults,q=V(T,w.ease),P=V(D,w.playbackEase),pe=P?Vt(P):null,Ae=!_(q.ease),Ne=Ae?q.ease:V(T,pe?"linear":w.ease),Ee=Ae?q.settlingDuration:V(x,w.duration),ke=V(p,w.delay),De=F||w.modifier,st=_(O)&&l>=me?I.none:_(O)?w.composition:O,rt=this._offset+(r?r._offset:0);Ae&&(q.parent=this);let M=NaN,X=NaN,Be=0,W=0;for(let m=0;m<l;m++){let N=c[m],Z=i||m,ae=a||c,Je=NaN,nt=NaN;for(let le in f)if(Nt(le)){let Y=_s(N,le),$e=Ht(N,le),ce=Yt(le,N,Y),E=f[le],G=ze(E);if(o&&!G&&(yt[0]=E,yt[1]=E,E=yt),G){let H=E.length,se=!Ge(E[0]);H===2&&se?(es.to=E,jt[0]=es,Ye=jt):H>2&&se?(Ye=[],E.forEach((ue,re)=>{re?re===1?(yt[1]=ue,Ye.push(yt)):Ye.push(ue):yt[0]=ue})):Ye=E}else jt[0]=E,Ye=jt;let Pe=null,te=null,ge=NaN,Oe=0,Ke=0;for(let H=Ye.length;Ke<H;Ke++){let se=Ye[Ke];Ge(se)?Re=se:(es.to=se,Re=es),Gt.func=null,Qt.func=null;let ue=Se(V(Re.composition,st),N,Z,ae,null,null),re=dt(ue)?ue:I[ue];!Pe&&re!==I.none&&(Pe=wt(N,ce));let ot=Pe?Pe._tail:null,he=r&&ot&&ot.parent.parent===r?ot:te,we=Se(Re.to,N,Z,ae,Gt,he),k;Ge(we)&&!_(we.to)?(Re=we,k=we.to):k=we;let Ie=Se(Re.from,N,Z,ae,Qt,he),z=Re.ease||Ne,qe=Se(z,N,Z,ae,null,he),ye=Q(qe)||_e(qe)?qe:z,it=!_(ye)&&!_(ye.ease),Mt=it?ye.ease:ye,Ut=it?ye.settlingDuration:Se(V(Re.duration,H>1?Se(Ee,N,Z,ae,null,he)/H:Ee),N,Z,ae,null,he),at=Se(V(Re.delay,Ke?0:ke),N,Z,ae,null,he),lt=Re.modifier||De,Ze=!_(Ie),vt=!_(k),xt=ze(k),Rr=xt||Ze&&vt,Ar=te?Oe:0,rs=te?Oe+at:at,ns=S(rt+rs,12),Nr=S(rt+Ar,12);!W&&(Ze||xt)&&(W=1);let fe=te;if(re!==I.none){let C=Pe._head;for(;C&&C._absoluteStartTime<=ns;)if(C._isOverridden||(fe=C),C=C._nextRep,C&&C._absoluteStartTime>=ns)for(;C;)Ot(C),C=C._nextRep}if(Rr){ee(xt?Se(k[0],N,Z,ae,Qt,he):Ie,h),ee(xt?Se(k[1],N,Z,ae,Gt,he):k,b);let C=ht(N,ce,Y,gt);h.t===y.NUMBER&&(fe?fe._valueType===y.UNIT&&(h.t=y.UNIT,h.u=fe._unit):(ee(C,ie),ie.t===y.UNIT&&(h.t=y.UNIT,h.u=ie.u)))}else vt?ee(k,b):te?Ts(te,b):ee(r&&fe&&fe.parent.parent===r?fe._value:ht(N,ce,Y,gt),b),Ze?ee(Ie,h):te?Ts(te,h):ee(r&&fe&&fe.parent.parent===r?fe._value:ht(N,ce,Y,gt),h);if(h.o&&(h.n=_t(fe?fe._toNumber:ee(ht(N,ce,Y,gt),ie).n,h.n,h.o)),b.o&&(b.n=_t(h.n,b.n,b.o)),h.t!==b.t){if(h.t===y.COMPLEX||b.t===y.COMPLEX){let C=h.t===y.COMPLEX?h:b,J=h.t===y.COMPLEX?b:h;J.t=y.COMPLEX,J.s=U(C.s),J.d=C.d.map(()=>J.n)}else if(h.t===y.UNIT||b.t===y.UNIT){let C=h.t===y.UNIT?h:b,J=h.t===y.UNIT?b:h;J.t=y.UNIT,J.u=C.u}else if(h.t===y.COLOR||b.t===y.COLOR){let C=h.t===y.COLOR?h:b,J=h.t===y.COLOR?b:h;J.t=y.COLOR,J.d=C.d.map(()=>0)}}if(h.u!==b.u){let C=b.u?h:b;C=Ss(N,C,b.u?b.u:h.u,!1)}if(b.d&&h.d&&b.d.length!==h.d.length){let C=h.d.length>b.d.length?h:b,J=C===h?b:h;J.d=C.d.map((Yr,Is)=>_(J.d[Is])?0:J.d[Is]),J.s=U(C.s)}let os=S(+Ut||g,12),Ps=gt[ce];xe(Ps)||(gt[ce]=null);let Er=$e?$e.set:null;Oe=S(rs+os,12);let Ft=h.d,Os=b.d,ws=b.s,ne={parent:this,id:$r++,property:ce,target:N,_value:null,_toFunc:Gt.func,_fromFunc:Qt.func,_ease:Vt(Mt),_fromNumbers:Ft?U(Ft):Rt,_toNumbers:Os?U(Os):Rt,_strings:ws?U(ws):Rt,_fromNumber:h.n,_toNumber:b.n,_numbers:Ft?U(Ft):Rt,_number:h.n,_unit:b.u,_modifier:lt,_currentTime:0,_startTime:rs,_delay:+at,_updateDuration:os,_changeDuration:os,_absoluteStartTime:ns,_absoluteUpdateStartTime:Nr,_absoluteEndTime:S(rt+Oe,12),_hasFromValue:Ze||xt?1:0,_tweenType:Y,_setter:Er,_valueType:b.t,_composition:re,_isOverlapped:0,_isOverridden:0,_renderTransforms:0,_inlineValue:Ps,_prevRep:null,_nextRep:null,_prevAdd:null,_nextAdd:null,_prev:null,_next:null};re!==I.none&&Kt(ne,Pe);let is=ne._valueType;if(is===y.COMPLEX)ne._value=Wt(ne,1,-1);else if(is===y.UNIT)ne._value=`${lt(ne._toNumber)}${ne._unit}`;else if(is===y.COLOR){let C=b.d;ne._value=`rgba(${S(C[0],0)},${S(C[1],0)},${S(C[2],0)},${C[3]})`}else ne._value=lt(ne._toNumber);isNaN(ge)&&(ge=ne._startTime),te=ne,Be++,Te(this,ne)}(isNaN(X)||ge<X)&&(X=ge),(isNaN(M)||Oe>M)&&(M=Oe),Y===A.TRANSFORM&&(Je=Be-Ke,nt=Be)}if(!isNaN(Je)){let le=0;R(this,Y=>{le>=Je&&le<nt&&(Y._renderTransforms=1,Y._composition===I.blend&&R(Ue.animation,$e=>{$e.id===Y.id&&($e._renderTransforms=1)})),le++})}}l||console.warn("No target found. Make sure the element you're trying to animate is accessible before creating your animation."),X?(R(this,m=>{m._startTime-m._delay||(m._delay-=X),m._startTime-=X}),M-=X):X=0,M||(M=g,this.iterationCount=0),this.targets=c,this.id=_(d)?gr:d,this.duration=M===g?g:et((M+this._loopDelay)*this.iterationCount-this._loopDelay)||g,this.onRender=L||w.onRender,this._ease=pe,this._delay=X,this.iterationDuration=M,!this._autoplay&&W&&this.onRender(this)}stretch(t){let s=this.duration;if(s===Le(t))return this;let r=t/s;return R(this,n=>{n._updateDuration=Le(n._updateDuration*r),n._changeDuration=Le(n._changeDuration*r),n._currentTime*=r,n._delay*=r,n._startTime*=r,n._absoluteStartTime*=r,n._absoluteUpdateStartTime*=r,n._absoluteEndTime*=r}),super.stretch(t)}refresh(){return R(this,t=>{let s=t._toFunc,r=t._fromFunc;(s||r)&&(r?(ee(r(),h),h.u!==t._unit&&t.target[be]&&Ss(t.target,h,t._unit,!0),t._fromNumbers=U(h.d),t._fromNumber=h.n):s&&(ee(ht(t.target,t.property,t._tweenType),ie),t._fromNumbers=U(ie.d),t._fromNumber=ie.n),s&&(ee(s(),b),t._toNumbers=U(b.d),t._strings=U(b.s),t._toNumber=b.o?_t(t._fromNumber,b.n,b.o):b.n))}),this.duration===g&&this.restart(),this}revert(){return super.revert(),Pt(this)}then(t){return super.then(t)}},yr=(e,t)=>v.editor?v.editor.addAnimation(e,t):new bt(e,t,null,0,!1).init();var Xr=(e,t)=>{if(oe(t,"<")){let s=t[1]==="<",r=e._tail,n=r?r._offset+r._delay:0;return s?n:n+r.duration}},Lt=(e,t)=>{let s=e.iterationDuration;if(s===g&&(s=0),_(t))return s;if(dt(+t))return+t;let r=t,n=e?e.labels:null,o=!xe(n),i=Xr(e,r),a=!_(i),c=zs.exec(r);if(c){let l=c[0],u=r.split(l),f=o&&u[0]?n[u[0]]:s,d=a?i:o?f:s,p=+u[1];return _t(d,p,l[0])}else return a?i:o?_(n[r])?s:n[r]:s};function Hr(e){return et((e.iterationDuration+e._loopDelay)*e.iterationCount-e._loopDelay)||g}function As(e,t,s,r,n,o){let a=dt(e.duration)&&e.duration<=g?s-g:s;t.composition&&Ce(t,a,1,1,B.AUTO);let c=r?new bt(r,e,t,a,!1,n,o):new tt(e,t,a);return t.composition&&c.init(!0),Te(t,c),R(t,l=>{let f=l._offset+l._delay+l.duration;f>t.iterationDuration&&(t.iterationDuration=f)}),t.duration=Hr(t),t}var br=0,ts=class extends tt{constructor(t={}){super(t,null,0),++br,this.id=_(t.id)?br:t.id,this.duration=0,this.labels={};let s=t.defaults,r=v.defaults;this.defaults=s?qt(s,r):r,this.composition=V(t.composition,!0),this.onRender=t.onRender||r.onRender;let n=V(t.playbackEase,r.playbackEase);this._ease=n?Vt(n):null,this.iterationDuration=0}add(t,s,r){let n=Ge(s),o=Ge(t);if(n||o){if(this._hasChildren=!0,n){let i=s,a=v.editor&&v.editor.addTimelineChild,c=r&&r.type==="Stagger"&&v.editor,l=Q(r)?r:null;if(l||c){let u=We(t),f=this.duration,d=this.iterationDuration,p=i.id,x=0,T=u.length,D=a?a(t,i,this.id,r,T):null,F=l||v.editor.resolveStagger(r.defaultValue);u.forEach(O=>{let L={...D||i};this.duration=f,this.iterationDuration=d,_(p)||(L.id=p+"-"+x);let w=Lt(this,F(O,x,u,null,this));As(L,this,w,O,x,u),x++})}else{let u=a?a(t,i,this.id,r):i,f=r&&r.type?r.defaultValue:r;As(u,this,Lt(this,f),t)}}else As(t,this,Lt(this,s));return this.composition&&this.init(!0),this}}sync(t,s){if(_(t)||t&&_(t.pause))return this;t.pause();let r=+(t.effect?t.effect.getTiming().duration:t.duration);!_(t)&&!_(t.persist)&&(t.persist=!0);let n=v.editor,o=n&&n.addTimelineChild;n&&n.addTimelineSync&&(s=n.addTimelineSync(t,s,this.id),n.addTimelineChild=null);let i=this.add(t,{currentTime:[0,r],duration:r,delay:0,ease:"linear",playbackEase:"linear"},s);return n&&(n.addTimelineChild=o),i}set(t,s,r){return _(s)?this:(s.duration=g,s.composition=I.replace,this.add(t,s,r))}call(t,s){return _(t)||t&&!Q(t)?this:(v.editor&&v.editor.addTimelineCall&&(s=v.editor.addTimelineCall(t,s,this.id)),this.add({duration:0,delay:0,onComplete:()=>t(this)},s))}label(t,s){return _(t)||t&&!_e(t)?this:(v.editor&&v.editor.addTimelineLabel&&(s=v.editor.addTimelineLabel(t,s,this.id)),this.labels[t]=Lt(this,s),this)}remove(t,s){return bs(We(t),this,s),this}stretch(t){let s=this.duration;if(s===Le(t))return this;let r=t/s,n=this.labels;R(this,o=>o.stretch(o.duration*r));for(let o in n)n[o]*=r;return super.stretch(t)}refresh(){return R(this,t=>{t.refresh&&t.refresh()}),this}revert(){return super.revert(),R(this,t=>t.revert,!0),Pt(this)}then(t){return super.then(t)}},vr=e=>v.editor?v.editor.addTimeline(e):new ts(e).init();var Ds={};Pr(Ds,{createDrawable:()=>Sr,createMotionPath:()=>xr,morphTo:()=>Cr});var ss=e=>{let s=We(e)[0];return!s||!mt(s)?console.warn(`${e} is not a valid SVGGeometryElement`):s};var Ns=(e,t,s,r,n)=>{let o=s+r,i=n?Math.max(0,Math.min(o,t)):(o%t+t)%t;return e.getPointAtLength(i)},Es=(e,t,s=0)=>r=>{let n=+e.getTotalLength(),o=r[ct],i=e.getCTM(),a=s===0;return{from:0,to:n,modifier:c=>{let l=s*n,u=c+l;if(t==="a"){let f=Ns(e,n,u,-1,a),d=Ns(e,n,u,1,a);return er(d.y-f.y,d.x-f.x)*180/je}else{let f=Ns(e,n,u,0,a);return t==="x"?o||!i?f.x:f.x*i.a+f.y*i.c+i.e:o||!i?f.y:f.x*i.b+f.y*i.d+i.f}}}},xr=(e,t=0)=>{let s=ss(e);if(s)return{translateX:Es(s,"x",t),translateY:Es(s,"y",t),rotate:Es(s,"a",t)}};var zr=e=>{let t=1;if(e&&e.getCTM){let s=e.getCTM();if(s){let r=Et(s.a*s.a+s.b*s.b),n=Et(s.c*s.c+s.d*s.d);t=(r+n)/2}}return t},Wr=(e,t,s)=>{let r=me,n=getComputedStyle(e),o=n.strokeLinecap,i=n.vectorEffect==="non-scaling-stroke"?e:null,a=o,c=new Proxy(e,{get(l,u){let f=l[u];return u===Bt?l:u==="setAttribute"?(...d)=>{if(d[0]==="draw"){let x=d[1].split(" "),T=+x[0],D=+x[1],F=zr(i),O=T*-r*F,L=D*r*F+O,w=r*F+(T===0&&D===1||T===1&&D===0?0:10*F)-L;if(o!=="butt"){let q=T===D?"butt":o;a!==q&&(l.style.strokeLinecap=`${q}`,a=q)}l.setAttribute("stroke-dashoffset",`${O}`),l.setAttribute("stroke-dasharray",`${L} ${w}`)}return Reflect.apply(f,l,d)}:Q(f)?(...d)=>Reflect.apply(f,l,d):f}});return e.getAttribute("pathLength")!==`${r}`&&(e.setAttribute("pathLength",`${r}`),c.setAttribute("draw",`${t} ${s}`)),c},Sr=(e,t=0,s=0)=>We(e).map(n=>Wr(n,t,s));var Cr=(e,t=.33)=>(s,r,n,o)=>{if(!(s.tagName||"").toLowerCase().match(/^(path|polygon|polyline)$/))throw new Error(`Can't morph a <${s.tagName}> SVG element. Use <path>, <polygon> or <polyline>.`);let a=ss(e);if(!a)throw new Error("Can't morph to an invalid target. 'path2' must resolve to an existing <path>, <polygon> or <polyline> SVG element.");if(!(a.tagName||"").toLowerCase().match(/^(path|polygon|polyline)$/))throw new Error(`Can't morph a <${a.tagName}> SVG element. Use <path>, <polygon> or <polyline>.`);let l=s.tagName==="path",u=l?" ":",",f=o?o._value:null;f&&s.setAttribute(l?"d":"points",f);let d="",p="";if(!t)d=s.getAttribute(l?"d":"points"),p=a.getAttribute(l?"d":"points");else{let x=s.getTotalLength(),T=a.getTotalLength(),D=Math.max(Math.ceil(x*t),Math.ceil(T*t));for(let F=0;F<D;F++){let O=F/(D-1),L=s.getPointAtLength(x*O),w=a.getPointAtLength(T*O),q=l?F===0?"M":"L":"";d+=q+S(L.x,3)+u+L.y+" ",p+=q+S(w.x,3)+u+w.y+" "}}return[d,p]};export{yr as animate,vr as createTimeline,Ds as svg};
/*! Bundled license information:

animejs/dist/modules/core/consts.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/globals.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/helpers.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/transforms.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/adapters/registry.js:
  (**
   * Anime.js - adapters - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/colors.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/values.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/render.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/styles.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/clock.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/animation/additive.js:
  (**
   * Anime.js - animation - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/engine/engine.js:
  (**
   * Anime.js - engine - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/animation/composition.js:
  (**
   * Anime.js - animation - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/timer/timer.js:
  (**
   * Anime.js - timer - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/targets.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/core/units.js:
  (**
   * Anime.js - core - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/easings/none.js:
  (**
   * Anime.js - easings - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/easings/eases/parser.js:
  (**
   * Anime.js - easings - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/animation/animation.js:
  (**
   * Anime.js - animation - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/timeline/position.js:
  (**
   * Anime.js - timeline - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/timeline/timeline.js:
  (**
   * Anime.js - timeline - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/svg/helpers.js:
  (**
   * Anime.js - svg - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/svg/motionpath.js:
  (**
   * Anime.js - svg - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/svg/drawable.js:
  (**
   * Anime.js - svg - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/svg/morphto.js:
  (**
   * Anime.js - svg - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/svg/index.js:
  (**
   * Anime.js - svg - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)

animejs/dist/modules/index.js:
  (**
   * Anime.js - ESM
   * @version v4.5.0
   * @license MIT
   * @copyright 2026 - Julian Garnier
   *)
*/
