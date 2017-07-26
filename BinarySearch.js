//Binary Search

var arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];


function bSearch(arr , target){
	var len = arr.length,
	end = len - 1,
	start = 0,
	found ;
	
	while(start <= end){
		mid = Math.floor((start+end)/2);
		found = arr[mid];
		if(target > found){
			start = mid + 1;
		} else if(target < found){
			end = mid - 1;
			
		} else {
			return mid;
		}
	}
	return -1;
}

//example.
