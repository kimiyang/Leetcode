var openLock = function(deadends, target) {
	let q = ['0000'];
	let res = 0;
	let visited = new Set();
	let counting = 0;
    if(deadends.find(n=>n==='0000'))return -1;
	while(q.length > 0) {
		let qsize = q.length;
		for(let j = 0;j < qsize; j++) {
			let current = q[j];
			if(visited.has(current)) {
				continue;
			}
			counting++;
			// console.log(counting)
			visited.add(current);
			if(current === target) {
				return res;
			}
			for(let i=0;i<4;i++) {
				let left = current.substr(0, i);
				let right = current.substr(i+1, 4);
				let down = (Number(current.charAt(i))+9) % 10;
				let up = (Number(current.charAt(i))+1) % 10;
				let next = left+down+right;
				if(!visited.has(next) && !(deadends.find(n=>n===next))) {
					q.push(next);
				}
				next = left+up+right;
				if(!visited.has(next) && !(deadends.find(n=>n===next))) {
					q.push(next);
				}
			}
		}
		res++;
		q = q.slice(qsize, q.length);
	}
    return -1;
};