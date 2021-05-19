$(function () {
	
	
	
	
	
	
$('.list-hr:last').hide()

	
class CaculatorDate {
	constructor(start){
		this.start = start;
		this.end = (new Date()).getTime()
	}
	
	getTimes() {
		var nn = this.end - this.start;
		return nn
	}
	getYears() {
		return Math.floor(this.getTimes() / (365 * 24 * 60 * 60 * 1000));
	}
	
	getMonths() {
		return Math.floor(this.getTimes() % (365 * 24 * 60 * 60 * 1000) / (30 * 24 * 3600 * 1000));
	}
	
	getDays() {
		return Math.floor(this.getTimes() / (24 * 3600 * 1000));
	}
	
	getHours() {
		return Math.floor(this.getTimes() % (24 * 3600 * 1000) / (3600 * 1000));
	}
	
	getMinutes() {
		return Math.floor((this.getTimes() % (24 * 3600 * 1000) % (3600 * 1000)) / (60 * 1000));
	}
	
	getSeconds() {
		return Math.floor((this.getTimes() % (24 * 3600 * 1000) % (3600 * 1000)) % (60 * 1000) / 1000);
	}
	
	getAutoTime() {
		if (this.getYears() > 0 ) {
		  return this.getYears() + "年";
		}else if (this.getMonths() >0 ) {
		  return this.getMonths() + "月";
		}else if (this.getDays() > 0 ) {
		  return this.getDays() + "天";
		}else if (this.getHours() > 0 ) {
		  return this.getHours() + "小时";
		}else if (this.getMinutes() > 0) {
		  return this.getMinutes() + "分钟";
		}else if (this.getSeconds() > 0) {
		  return this.getSeconds() + "秒";
		}
	}
}

var ss = (new CaculatorDate(1621148150230)).getAutoTime();


//计算当前的文章多久前创建的
$(function () {
  var m = $(".create_time");
  m.each(function(){
   var n = $(this).text();
   var nd = (new CaculatorDate(n)).getAutoTime();
   $(this).text('创建:'+nd+"前");
  });
  
  var m = $(".update_time");
  m.each(function(){
   var n = $(this).text();
   var nd = (new CaculatorDate(n)).getAutoTime();
   $(this).text('更新:'+nd+"前");
});
});
	
	
	
	
	
	
	
	
	
	
})