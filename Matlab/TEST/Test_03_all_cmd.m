% NOTE: 
% Test script N3
% Testing the device's response to various types of command errors.
%


%% include 'aDevice'

Fern.load('aDevice')

%%


clc

COM_port = 3;

% cell array with cmds in col 1 and err_no in col 2
Test_table = {
"ABCD", [];
"ABDC", [];
"ACBD", [];
"ACDB", [];
"ADBC", [];
"ADCB", [];
"BACD", [];
"BADC", [];
"BCAD", [];
"BCDA", [];
"BDAC", [];
"BDCA", [];
"CABD", [];
"CADB", [];
"CBAD", [];
"CBDA", [];
"CDAB", [];
"CDBA", [];
"DABC", [];
"DACB", [];
"DBAC", [];
"DBCA", [];
"DCAB", [];
"DCBA", [];

"1234", [];
"1243", [];
"1324", [];
"1342", [];
"1423", [];
"1432", [];
"2134", [];
"2143", [];
"2314", [];
"2341", [];
"2413", [];
"2431", [];
"3124", [];
"3142", [];
"3214", [];
"3241", [];
"3412", [];
"3421", [];
"4123", [];
"4132", [];
"4213", [];
"4231", [];
"4312", [];
"4321", [];

"XBCD", [];
"AXCD", [];
"ABXD", [];
"ABCX", [];

"XXCD", [];
"XBXD", [];
"XBCX", [];
"AXXD", [];
"AXCX", [];
"ABXX", [];

"XXXD", [];
"XXCX", [];
"XBXX", [];
"AXXX", [];

"XXXX", [];

"X234", [];
"1X34", [];
"12X4", [];
"123X", [];

"XX34", [];
"X2X4", [];
"X23X", [];
"1XX4", [];
"1X3X", [];
"12XX", [];

"XXX4", [];
"XX3X", [];
"X2XX", [];
"1XXX", [];

"XXXX", [];

"1BCD", 301;
"2BDC", 301;
"3CBD", 301;
"4CDB", 301;
"A2BC", 301;
"AD12", 301;
"B4CD", 301;
"B3DC", 301;
"B212", 301;
"43AC", 301;
"BD2A", 301;

"2243", 302;
"3324", 302;
"4342", 302;
"1223", 302;
"1412", 302;
"2434", 302;
"2343", 302;
"2212", 302;
"4313", 302;
"2421", 302;
"//.*", 301;
"4317", 301;
"0223", 301;

"CACD", 302;
"CADD", 302;
"ABAD", 302;
"CBBA", 302;
"CDCB", 302;
"CBBA", 302;
"DABA", 302;
"AACB", 302;
"DCAC", 302;
"DBBC", 302;

"3134", 302;
"3144", 302;
"1214", 302;
"3221", 302;
"3411", 302;
"3221", 302;
"4121", 302;
"1132", 302;
"4313", 302;
"4223", 302;

"A", 200;
"AB", 200;
"ABC", 200;
"CBCDE", 200;
"ABCDD", 200;
"", 200;
"rgddj", 200;




"*IDN??", 103
"*", 103
"*12", 103
"*12345", 103
"*1234567", 103

"*1234", 102
"*IDD?", 102
"*    ", 102
"*ABCD", 102

"*123", 101
"*RSS", 101
"*   ", 101
"*ABC", 101


};


N = size(Test_table, 1);
Status_arr = false(1, N);

Box = Hall_box(COM_port);

try
    for i = 1:N
        CMD = Test_table{i, 1};
        err_no_exp = Test_table{i, 2};
        disp([num2str(i) '/' num2str(N) ' : ' char(CMD)])
        [~, err_no, ~] = Box.set_relay(CMD);
        disp(['    <' num2str(err_no) '> = <' num2str(err_no_exp) '>']);
        
        Test_table{i, 3} = err_no;

        if isempty(err_no) && isempty(err_no_exp) 
            status = true;
        else
            status = err_no == err_no_exp;
        end

        if status
            Status_arr(i) = true;
            disp('    PASS')
        else
            Status_arr(i) = false;
            disp('    FAIL')
        end
    end

catch err
    delete(Box);
    warning([newline 'Device is closed in error section'])
    rethrow(err);
end


delete(Box)
disp([newline 'Device is closed'])


if any(~Status_arr)
    Test_table(~Status_arr, :)
else
    disp('All tests passed.')
end





















